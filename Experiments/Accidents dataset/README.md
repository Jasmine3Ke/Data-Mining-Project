## 實驗介紹
這個實驗使用兩種模型進行 pattern set mining，分別是 Binaps 與 SLIM  
使用的資料集是 Accident.dat dataset，來自  http://fimi.uantwerpen.be/data/ 
大小為 340183 x 468。


### 執行 Binaps
若沒有指定 hidden_dimension，則預設為資料集本身的 columns 數量。
```
cd ../Binaps_code/  

python main.py --input ../Experiments/Accidents dataset/accidents.dat
```

測試不同大小的 hidden dimension：
```
python main.py --input accidents.dat --hidden_dim [hidden_dimension]
```  

### 執行 SLIM
確認安裝 skmine 套件後，執行下方指令即可：
```
python slim.py 
```
SLIM 中 k 的數量可從 slim.py 裡面自行調整，預設為 50。

## 實驗結果

### 實驗一 兩模型找出的 pattern 數量比較
參數設定：  
Binaps: 使用預設參數  
SLIM: K(Number of non-singleton itemsets to mine) = 1000  
(因為時間關係將 slim 的 k 設 1000，論文中則是花了 21h 找出了 12261 patterns)

| 模型 | pattern 數量 |
|-------|:-----:|
| Binaps|  83  |
| SLIM  |  1198  |


### 實驗二 兩模型的時間比較
參數設定：  
Binaps: 使用預設參數  
SLIM: K(Number of non-singleton itemsets to mine) = 1000  

GPU: GeForce GTX 1080  
CPU: Intel Xeon E5-2683 v3  

|  模型 | 時間(second) |
|-------|:-----:|
| Binaps(GPU) | 7 m |
| SLIM(CPU)   | 180 m |

### 實驗三 Binaps使用不同hidden dimension比較
參數設定：  
Binaps: 以下表格的每個實驗結果都只調整 hidden dimension size，其餘參數接使用預設參數  
以下表格的每個實驗結果皆在 GPU: GeForce GTX 1080 上執行  

|  hidden dim size | 25 | 50 | 100 | 150 | 200 | 300 | 400 | 468 (預設) | 1000 | 2000 | 3000
|-------|:-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| #patterns | 25 | 45 | 75 | 77 | 89 | 88 | 89 | 91 | 115 | 48 | 35 |
| runtime   | 202 s | 207 s | 215s | 213s | 218s | 235s | 238s | 180s | 300s | 600s | 720s |
