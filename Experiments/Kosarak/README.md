## 實驗介紹
這個實驗使用兩種模型進行 pattern set mining，分別是 Binaps 與 SLIM  
使用的資料集是 unchoice-Kosarak-5.25.txt dataset，來自 http://fimi.uantwerpen.be/data/
大小為 505217 x 22985。


### 執行 Binaps
若沒有指定 hidden_dimension，則預設為資料集本身的 columns 數量。
```
cd ../Binaps_code/  

python main.py --input ../Experiments/Kosarak/unchoice-Kosarak-5.25.txt
```

測試不同大小的 hidden dimension：
```
python main.py --input ../Experiments/Kosarak/unchoice-Kosarak-5.25.txt --hidden_dim [hidden_dimension]
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
SLIM: K(Number of non-singleton itemsets to mine) = 50  
(因為資料集 columns 數的關係只使用到 CPU 訓練，因此時間上並不足以讓模型收斂)
(因為時間關係將 slim 的 k 設 1000，論文中則是花了 21h 找出了 12261 patterns)

| 模型 | pattern 數量 |
|-------|:-----:|
| Binaps|  5  |
| SLIM  |  59  |


### 實驗二 兩模型的時間比較
參數設定：  
Binaps: 使用預設參數  
SLIM: K(Number of non-singleton itemsets to mine) = 50

CPU: Intel Xeon E5-2683 v3  

|  模型 | 時間(second) |
|-------|:-----:|
| Binaps(CPU) | 58h |
| SLIM(CPU)   | 4s |

