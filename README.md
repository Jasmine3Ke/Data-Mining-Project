# Data Mining Project

## Requirements
* Pytorch
* Scipy
* Pandas
* Numpy
* Skmine

## Implementation Details
**Dataset → the corresponding device**
* Retail.dat → Nvidia GeForce GTX 1070 GPU, Intel Cascade Lake
* Kosarak.dat → Intel Xeon E5-2683 v3 CPU (Binaps, SLIM)
* DMHW1_data.dat → Nvidia GeForce GTX 1080 GPU(Binaps), Intel Xeon E5-2683 v3 CPU(SLIM)
* Accidents.dat → Nvidia GeForce GTX 1080 GPU (Binaps), Intel Xeon E5-2683 v3 CPU(SLIM)

## Datasets
* retail.dat
  * **Description:** Retail market basket data from an anonymous Belgian retail store
  * **Link:** http://fimi.uantwerpen.be/data/ 
* kosarak.dat
  * **Description:** Click-stream data of a hungarian on-line news portal
  * **Link:** http://fimi.uantwerpen.be/data/ 
* accidents.dat
  * **Description:** Traffic accident data
  * **Link:** http://fimi.uantwerpen.be/data/ 
* DMHW1_data.csv
  * **Description:** The retail market data from the class of data mining homework 1

## 程式碼運行

本團隊如何運行各個程式碼的readme文件都寫在 Experiments 中的各個資料集的readme中

執行 
```
cd ../Binaps_code/  
python main.py --input DM_Project_Group08/Experiments/dataset/dataset.dat
```
將dataset換成不同名字，就可以在不同資料集上得到結果
