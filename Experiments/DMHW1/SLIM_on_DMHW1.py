from skmine.itemsets import SLIM
import csv
import time

input_file = "DMHW1_data.csv"
output_file = "DMHW1_SLIM_patterns.txt"

# 把資料轉成適當的格式
with open(input_file, newline = "") as csvF:
    rows = csv.reader(csvF)

    header = next(rows)
    items_dict = {}
    for index, value in enumerate(header):
        items_dict[index] = value

    Data = []
    for row in rows:
        tmp = [items_dict[index] for index, value in enumerate(row) if value == "True"] 
        Data.append(tmp)

# 找 pattern sets
start = time.time()
output = SLIM(k=20000).fit(Data).discover(singletons=False, usage_tids=True)
end = time.time()

# 把找出來的 patterns 記錄起來
with open(output_file, "w") as f:
    for pattern in output.index:
        f.write(str(pattern) + "\n")

print("SLIM exetution time: ", int(end - start), " seconds")
print("number of patterns: ", len(output))
