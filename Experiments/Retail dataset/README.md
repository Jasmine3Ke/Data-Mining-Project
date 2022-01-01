# 實驗介紹

本實驗使用 Binaps & SLIM 進行 pattern set mining，資料集上是使用Retail.dat資料集，來自 http://fimi.uantwerpen.be/data/
資料集大小為88162*16469。

# 執行方式
## Binaps
```
cd ../Binaps_code/  
python main.py --input DM_Project_Group08/Experiments/Retail dataset/retail.dat --batch_size [#batch size] --hidden_dim=[dim size]
```
input可以依據自己的資料集放在哪裡做調整，也可以調整batch_size和hidden dimension，在這個實驗中我們是使用預設的batch size，但有針對hidden dimension做調整
## SLIM
確認安裝 skmine 套件後，執行下方指令即可：
```
python Retail_on_SLIM.py
```
SLIM 中 k 的數量可從 Retail_on_SLIM.py 裡面的變數 k_num 自行調整，預設為 50。
# 實驗結果

因為依照本來的hidden dimension跑的話，會有GPU記憶體不足的問題，因此我們有針對hidden dimension做調整
retail_hidden_35.binaps.patterns 是將hidden_dim設定成35找出來的patterns
retail_hidden_8500.binaps.patterns 是將hidden_dim設定成8500找出來的patterns
