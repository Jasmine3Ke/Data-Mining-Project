## 實驗介紹
這個實驗使用兩種模型進行 pattern set mining，分別是 Binaps 與 SLIM  
使用的資料集是 data mining HW1 所提供的資料集，大小為 10000 * 1000  


## 執行方式
請先將資料集解壓縮  
```
unzip DMHW1_data.zip
```

### 執行 Binaps
請將 BINAPS_on_DMhw1.py 這份檔案複製到 DM_Project_Group08/Binaps_code/ 下：
```
cp BINAPS_on_DMHW1.py ../../Binaps_code/
```
將工作目錄移動到DM_Project_Group08/Binaps_code/ 下：
```
cd ../../Binaps_code/
```
確認相關套件都已安裝後，執行下方指令即可：
```
python BINAPS_on_DMHW1.py
```

測試不同大小的 hidden dimension：
```
python BINAPS_on_DMHW1.py --hidden_dim=[dim size]
```  

模型的其餘可調參數請自行參考 BINAPS_on_DMHW1.py

### 執行 SLIM
確認安裝 skmine 套件後，執行下方指令即可：
```
python SLIM_on_DMHW1.py 
```

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
