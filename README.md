# Helmet-Detection
本項目主要基於YoloV5s-V5.0版本實現工地上安全帽佩戴的檢測，因此本項目的主要實現背景是在Jetson Nano上部署好安全帽佩戴檢測的代碼，當然，在Windows/Linux上同樣可以實現，並且本項目包含TensorRT加速使其能夠在邊緣硬件平台上能夠更快更實時的處理數據，再次**强調**本項目使用的YoloV5是屬於**YoloV5s**網絡是屬於模型最小的，並且版本是**V5.0**（各個版本不是很兼容各版本有點差別）

![效果圖1](https://z3.ax1x.com/2021/08/17/f4v1Z8.jpg)  
# Requirement
```
Pillow
torch>=1.7.0
torchvision>=0.8.0
numpy>=1.18.5
matplotlib>=3.2.2
opencv-python>=4.1.2
PyYAML>=5.3.1
scipy>=1.4.1
tqdm>=4.41.0
seaborn
pycuda
```

# Quick start
- 步驟一 : 配置好對應的環境並且克隆項目到本地
```
$ git clone https://github.com/tomleee012/HelmetDetection.git
$ cd HelmetDetection
```
- 步驟二 ：在TensorRT加速下YoloV5s推理
```
$ cd helmet_yolov5
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa  # rtsp stream
                            http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8  # http stream

$ 例子：python detect.py --source test.jpg --weights helmet.pt
```

# Helmet Dataset
> 注意：下面兩個格式的數據集中的內容都是一樣的只不過是內容存放的格式以及內容需要的文件格式不同而已，二者可以相互轉換
- 安全帽VOC格式數據集
```
# 百度網盤鏈接：https://pan.baidu.com/s/1dE23iElE3iGVdsPfQYm3jg
# 提取碼：ir9x
```
- 安全帽Yolo格式数据集
```
# 百度網盤鏈接：https://pan.baidu.com/s/1CceCFIYzpBjjPcCe4_dr7g
# 提取碼：gyre
```

# How to train
- 準備好安全帽的yolo格式數據集（已上傳如上）和官方YoloV5s權重文件
```
# yoloV5s權重百度網盤鏈接：https://pan.baidu.com/s/1PPEDV2UZsPLpugEAEW2wGg
# 提取碼：6pfy
```
- （可選）製作自己的數據集，收集好圖像並命名好使用Labelbox 、CVAT 、精靈標註助手等標註工具標註生成xml文件並且文件格式放置參照VOC數據集格式如下其中Main文件的txt文件可通過```../utils/generate_txt.py```生成
```
---|
   |---Annotations----.xml
   |
   |---JPEGImages-----.jpg
   |
   |---Main-----------|
                      |--train.txt
                      |--val.txt
                      |--trainval.txt
                      |--test.txt
```
- （可選）將VOC格式數據集轉換成yolo格式數據集，在```../utils/gen_yolo_format.py```生成yolo格式數據集如下格式
```
---|
   |---images--|
   |           |--test
   |           |--train
   |           |--val
   |
   |---labels--|
               |--train
               |--val
               |--test
```
- 複製YoloV5官方的代碼到本地
```
$ git clone https://github.com/ultralytics/yolov5.git
```
- 準備好環境
```
$ cd yolov5
$ pip install -r requirements.txt
```
- 創建配置文件修改```data/custom_data.yaml```文件
```
# 設置數據集的路徑
train: data/Safety_Helmet_Train_dataset/score/images/train
val: data/Safety_Helmet_Train_dataset/score/images/val

# 分類數量
nc: 2

# 類別名稱
names: ['person', 'hat']
```
- 在models文件夾中選擇需要訓練的模型這裡選擇的是yoloV5s訓練並修改配置存放好為```yolov5s.yaml```
```
# 這裡只需要修改類別數量即可
nc: 2  # number of classes
```
- 執行訓練文件
```
$ python train.py --epochs 200 --data custom_data.yaml --cfg yolov5s.yaml --weights yolov5s.pt --device 0
```
- 在路徑下會生成runs文件夾裡面找到weights裡的best.pt就是訓練好的權重

# Results
- 檢測分類為person和hat分別代表沒戴安全帽和戴安全帽
![效果圖2](https://z3.ax1x.com/2021/08/17/f4vYGj.jpg)  
- 下圖為訓練的一個指標結果圖
![效果圖3](https://z3.ax1x.com/2021/08/17/f4vcW9.png)

# Reference
- [YoloV5](https://github.com/ultralytics/yolov5)

