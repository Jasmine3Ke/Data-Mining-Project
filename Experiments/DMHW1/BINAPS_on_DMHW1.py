from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.distributions as tdist
import torch.optim as optim
from torch.optim.lr_scheduler import MultiStepLR
from torch.utils.data import Dataset, DataLoader

import os
import pandas as pd
import numpy as np
import math

import dataLoader as mydl
import my_layers as myla
import my_loss as mylo
import network as mynet
import time

input_file = "../Experiments/DMHW1/DMHW1_data.csv"
output_file = "../Experiments/DMHW1/DMHW1_Binaps_patterns.txt"

def readCsvFile(csv_file):
    df = pd.read_csv(csv_file)
    df.replace(to_replace ="True", value ="1")
    df.replace(to_replace ="False", value ="0")
    return np.single(df)

class CsvDataset(Dataset):
    def __init__(self, csv_file, train_proportion, is_training, device_cpu):
        data = readCsvFile(csv_file)
        self.data = np.asarray(data)
        self.sparsity = np.count_nonzero(self.data)/np.prod(self.data.shape)
        if is_training:
            ran = np.arange(0,math.ceil(train_proportion*self.data.shape[0]))
        else:
            ran = np.arange(math.ceil(train_proportion*self.data.shape[0]),self.data.shape[0])
        self.data = torch.from_numpy(self.data[ran,:])#, device=device_cpu)

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, index):
        return self.data[index,:], self.data[index,:]

    def matmul(self, other):
        return self.data.matmul(other)

    def nrow(self):
        return self.data.shape[0]
    
    def ncol(self):
        return self.data.shape[1]

    def getSparsity(self):
        return self.sparsity

def learn(input, lr, gamma, weight_decay, epochs, hidden_dim, train_set_size, batch_size, test_batch_size, log_interval, device_cpu, device_gpu):
    kwargs = {}

    trainDS = CsvDataset(input, train_set_size, True, device_cpu)
    train_loader = torch.utils.data.DataLoader(trainDS,
        batch_size=batch_size, shuffle=True, **kwargs)

    test_loader = torch.utils.data.DataLoader(CsvDataset(input, train_set_size, False, device_cpu),
        batch_size=test_batch_size, shuffle=True, **kwargs)
    
    if hidden_dim == -1:
        hidden_dim = trainDS.ncol()

    new_weights = torch.zeros(hidden_dim, trainDS.ncol(), device=device_gpu)
    mynet.initWeights(new_weights, trainDS.data)
    new_weights.clamp_(1/(trainDS.ncol()), 1)
    bInit = torch.zeros(hidden_dim, device=device_gpu)
    nn.init.constant_(bInit, -1)

    model = mynet.Net(new_weights, bInit, trainDS.getSparsity(), device_cpu, device_gpu).to(device_gpu)
    optimizer = optim.Adam(model.parameters(), lr=lr)

    lossFun = mylo.weightedXor(trainDS.getSparsity(), weight_decay, device_gpu)

    scheduler = MultiStepLR(optimizer, [5,7], gamma=gamma)
    for epoch in range(1, epochs + 1):
        mynet.train(model, device_cpu, device_gpu, train_loader, optimizer, lossFun, epoch, log_interval)

        mynet.test(model, device_cpu, device_gpu, test_loader, lossFun)
        scheduler.step()

    return model, new_weights, trainDS

def main():
    # Training settings
    parser = argparse.ArgumentParser(description='Binary Pattern Network implementation')
    parser.add_argument('--train_set_size', type=float, default=.9,
                        help='proportion of data to be used for training')
    parser.add_argument('--batch_size', type=int, default=64,
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test_batch_size', type=int, default=64,
                        help='input batch size for testing (default: 64)')
    parser.add_argument('--epochs', type=int, default=10,
                        help='number of epochs to train (default: 10)')
    parser.add_argument('--lr', type=float, default=0.01,
                        help='learning rate (default: 0.01)')
    parser.add_argument('--weight_decay', type=float, default=0,
                        help='weight decay for L2 norm (default 0)')
    parser.add_argument('--gamma', type=float, default=0.1,
                        help='Learning rate step gamma (default: 0.1)')
    parser.add_argument('--seed', type=int, default=1,
                        help='random seed (default: 1)')
    parser.add_argument('--log_interval', type=int, default=10,
                        help='how many batches to wait before logging training status')
    parser.add_argument('--save_model', action='store_true', default=False,
                        help='save the current Model')
    parser.add_argument('--hidden_dim', type=int, default=-1,
                        help='size for the hidden layer (default: #features)')
    parser.add_argument('--thread_num', type=int, default=16,
                        help='number of threads to use (default: 16)')
    args = parser.parse_args()

    torch.manual_seed(args.seed)

    torch.set_num_threads(args.thread_num)

    device_cpu = torch.device("cpu")
    
    if not torch.cuda.is_available():
        device_gpu = device_cpu
        print("WARNING: Running purely on CPU. Slow.")
    else:
        device_gpu = torch.device("cuda")

    start = time.time()

    model, weights, train_data = learn(input_file, args.lr, args.gamma, args.weight_decay, args.epochs, args.hidden_dim, args.train_set_size, args.batch_size, args.test_batch_size, args.log_interval, device_cpu, device_gpu)

    if args.save_model:
        torch.save(model.state_dict(), "ternary_net.pt")

    df = pd.read_csv(input_file)
    items_dict = {}
    for index, value in enumerate(df.columns):
        items_dict[index] = value

    with torch.no_grad():
        pattern_num = 0
        with open(output_file,'w') as patF:
            for hn in myla.BinarizeTensorThresh(weights, .2):
                pat = torch.squeeze(hn.nonzero())
                supp_full = (train_data.matmul(hn.cpu()) == hn.sum().cpu()).sum().cpu().numpy()
                supp_half = (train_data.matmul(hn.cpu()) >= hn.sum().cpu()/2).sum().cpu().numpy()
                if hn.sum() >= 2:
                    pattern_num += 1
                    # 把找出來的 pattern sets 記錄起來
                    tmp = ""
                    for pattern in pat.cpu().numpy():
                        tmp += (items_dict[pattern] + ", ")
                    patF.write(tmp[:-2] + "\n")
    
    end = time.time()

    print("BINAPS exetution time: ", int(end - start), " seconds")
    print("number of pattern set: ", pattern_num)

if __name__ == '__main__':
    main()
