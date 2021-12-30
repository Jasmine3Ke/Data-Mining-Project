## 實驗介紹
這個實驗使用兩種模型進行 pattern set mining，分別是 Binaps 與 SLIM  
使用的資料集是 data mining HW1 所提供的資料集，大小為 10000 * 1000  


## 執行方式
請先將資料集解壓縮  

### 執行 Binaps
請將 BINAPS_on_DMhw1.py 這份檔案移動到 DM_Project_Group08/Binaps_code/ 下

確認相關套件都已安裝後，執行下方指令即可：
```
python BINAPS_on_DMhw1.py
```

測試不同大小的 hidden dimension：
```
python BINAPS_on_DMhw1.py --hidden_dim=[dim size]
```  

模型的其餘可調參數請自行參考 BINAPS_on_DMhw1.py

### 執行 SLIM
確認安裝 skmine 套件後，執行下方指令即可：
```
python SLIM_on_DMhw1.py 
```

## 結果
