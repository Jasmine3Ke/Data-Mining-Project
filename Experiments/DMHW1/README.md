## 實驗介紹
這個實驗使用兩種模型進行 pattern set mining，分別是 Binaps 與 SLIM  
使用的資料集是 data mining HW1 所提供的資料集，大小為 10000 * 1000  


## 執行方式
請先將資料集解壓縮  
```
unzip DMHW1_data.zip
```

### 執行 Binaps
請將 BINAPS_on_DMhw1.py 這份檔案移動到 DM_Project_Group08/Binaps_code/ 下
```
cp BINAPS_on_DMHW1.py ../../Binaps_code/
```
將工作目錄移動到DM_Project_Group08/Binaps_code/ 下
```
cd ../../Binaps_code/
```
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
