# 實驗介紹

* 本實驗使用 Binaps & SLIM 進行 pattern set mining
* 使用Retail.dat資料集，來自 http://fimi.uantwerpen.be/data/
* 資料集大小為88162*16469。

# 執行方式
## Binaps
```
cd ../Binaps_code/  
python main.py --input DM_Project_Group08/Experiments/Retail dataset/retail.dat --batch_size [#batch size] --hidden_dim=[dim size]
```
input 可以依據自己的資料集放在哪裡做調整，也可以調整 batch_size 和 hidden dimension，在這個實驗中我們是使用預設的 batch size，但有針對 hidden dimension 做調整
## SLIM
確認安裝 skmine 套件後，執行下方指令即可：
```
python Retail_on_SLIM.py
```
SLIM 中 k 的數量可從 Retail_on_SLIM.py 裡面的變數 k_num 自行調整，預設為 50。
# 實驗結果
## 實驗一 用 Binaps 執行 pattern set mining
GPU: GeForce GTX 1070

用 Binaps 執行的時候，因為依照本來的 hidden dimension 跑的話，會有 GPU 記憶體不足的問題，因此我們有針對 hidden dimension 做調整

retail_hidden_35.binaps.patterns 是將 hidden_dim 設定成 35 找出來的 patterns

retail_hidden_8500.binaps.patterns 是將 hidden_dim 設定成 8500 找出來的 patterns
## 實驗二 用 SLIM 執行 pattern set mining
CPU: Intel Cascade Lake

這部分的實驗是更改參數 k 觀察最後找出的 patterns 數量的差異。
k 的調整是從預設的 50 開始調整，很快就發現當 k 的大小足夠找完所有的 patterns 之後，不管k調的多大，執行時間都幾乎不會改變，patterns 的數量也會穩定在一個數值

|  k | 50 | 300 | 500 | 700 | 1000 | 20000 | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Patterns | 50 | 206 | 206 | 206 | 206 | 206 | 206 | 
| Runtime  | 0.64s | 19.8s | 20.5s | 19.5s | 19.7s | 19.7s |
