## 實驗介紹
這個實驗使用兩種模型進行 pattern set mining，分別是 Binaps 與 SLIM  
使用的資料集是 Accident.dat dataset，來自  http://fimi.uantwerpen.be/data/ 
大小為 340183 x 468。


### 執行 Binaps
```
cd ../Binaps_code/  

python main.py --input accidents.dat
```
若沒有指定 hidden_dimension，則預設為資料集本身的 columns 數量。


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
SLIM: K(Number of non-singleton itemsets to mine) = 20000  

| 模型 | pattern 數量 |
|-------|:-----:|
| Binaps|  278  |
| SLIM  |  292  |


### 實驗二 兩模型的時間比較
參數設定：  
Binaps: 使用預設參數  
SLIM: K(Number of non-singleton itemsets to mine) = 20000  

GPU: GeForce GTX 1080  
CPU: Intel Xeon E5-2683 v3  

|  模型 | 時間(second) |
|-------|:-----:|
| Binaps(GPU) | 15 s |
| Binaps(CPU) | 37 s |
| SLIM(CPU)   | 70 s |

### 實驗三 Binaps使用不同hidden dimension比較
參數設定：  
Binaps: 以下表格的每個實驗結果都只調整 hidden dimension size，其餘參數接使用預設參數  
以下表格的每個實驗結果皆在 GPU: GeForce GTX 1080 上執行  

|  hidden dim size | 100 | 300 | 700 | 900 | 1000(預設) | 2000 | 3000 |
|-------|:-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| #patterns | 83 | 131 | 224 | 250 | 278 | 421 | 550 |
| runtime   | 14 s | 15 s | 15s | 14s | 15s | 16s | 17s|
