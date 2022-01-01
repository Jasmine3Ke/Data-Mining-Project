from skmine.itemsets import SLIM
import numpy as np
import time

def readDatFile(dat_file):

  ncol = -1
  nrow = 0
  with open(dat_file) as datF:
    # read .dat format line by line
    l = datF.readline()
    while l:
      # drop newline
      l = l[:-1]
      if l == "":
        continue
      if l[-1] == " ":
        l = l[:-1]
      # get indices as array
      sl = l.split(" ")
      sl = [int(i) for i in sl]
      maxi = max(sl)
      if (ncol < maxi):
        ncol = maxi
      nrow += 1
      l = datF.readline()
  data = np.zeros((nrow, ncol), dtype=np.single)
  with open(dat_file) as datF:
    # read .dat format line by line
    l = datF.readline()
    rIdx = 0
    while l:
      # drop newline
      l = l[:-1]
      if l == "":
        continue
      if l[-1] == " ":
        l = l[:-1]
      # get indices as array
      sl = l.split(" ")
      idxs = np.array(sl, dtype=int)
      idxs -= 1
      # assign active cells
      data[rIdx, idxs] = np.repeat(1, idxs.shape[0])
      rIdx += 1
      l = datF.readline()

  return data

#with open('data/uchoice-Kosarak-5-25.txt', 'r') as f:
#tmp = f.readlines()

data = readDatFile('accidents.dat')
print(data.shape)

start = time.time()
slim = SLIM(k=50).fit(data).discover(singletons=False, usage_tids=True)
end = time.time()

print(slim)
print(len(slim))
print(end-start)
