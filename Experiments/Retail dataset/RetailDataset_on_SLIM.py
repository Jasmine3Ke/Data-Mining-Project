from skmine.itemsets import SLIM
import time

data = []
with open('C:/Users/Jacob/Desktop/研究所/資料探勘/binaps/Data/Test_retail/retail.dat', 'r') as f:
    for line in f.readlines():
        line_li = line.split(' ')
        del line_li[len(line_li)-1]
        data.append(line_li)

start = time.process_time()
result = SLIM(k=300).fit(data).discover(singletons=False, usage_tids=True)
end = time.process_time()
print(result)
print("執行時間：%f 秒" % (end - start))
