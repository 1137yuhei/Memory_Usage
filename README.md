# memory_usage
ロボットシステム学授業用
メモリ使用率をトピックから出力するROS2のパッケージ

[![test](https://github.com/1137yuhei/Memory_Usage/actions/workflows/test.yml/badge.svg)](https://github.com/1137yuhei/Memory_Usage/actions/workflows/test.yml)

##  ノード概要

###  MemoryUsagePiblisherノード

- ```MemoryUsagePiblisher```ノードはシステムのメモリの使用率を1秒ごとに計測し、トピックにパブリッシュする

###  listenerノード

- テスト用
- メッセージをサブスクライブして受け取る

##  トピック

###  memory_usageトピック

- このトピックはFloat64型のメッセージを受け取ることができる

## 必要なソフトウェア

- Python
  - テスト済みバージョン：3.7~3.11
- ROS 2 foxy

## テスト環境

- ubuntu 22.04 LTS


## 使用方法

### パッケージのセットアップ

- psutilをインストールする
```
sudo apt install python3-pip
pip install psutil
```
- リポジトリをクローン
```
cd ~/ros2_ws/src
git clone https://github.com/1137yuhei/Memory_Usage.git
```
- ディレクトリに移動
```
cd ~/ros2_ws
colon build
```
###  ノードの実行

####  一つの端末で実行する方法

  `ros2 run talk_listen.launch.py`

####  二つの端末で実行する方法

  - 一つ目の端末で以下のコマンドを実行

  `ros2 run mypkg memory_usage_publisher`

  - 二つ目の端末で以下のコマンドを実行

  `ros2 run mypkg listener`

## 実行結果

### 一つの端末で実行した例
```
[listener-2] [INFO] [1736062114.849651170] [memory_listener]: Memory_listener: 8.8%
[memory_usage_publisher-1] [INFO] [1736062115.848540585] [memory_usage_pub]: Publishing: 8.8%
[listener-2] [INFO] [1736062115.849522338] [memory_listener]: Memory_listener: 8.8%
[memory_usage_publisher-1] [INFO] [1736062116.848671766] [memory_usage_pub]: Publishing: 8.8%
[listener-2] [INFO] [1736062116.849681993] [memory_listener]: Memory_listener: 8.8%
[memory_usage_publisher-1] [INFO] [1736062117.848692131] [memory_usage_pub]: Publishing: 8.8%
[listener-2] [INFO] [1736062117.849535256] [memory_listener]: Memory_listener: 8.8%
[memory_usage_publisher-1] [INFO] [1736062118.848518762] [memory_usage_pub]: Publishing: 8.8%
...
```
### 二つつの端末で実行した例

- 一つ目の端末
```
[INFO] [1736054814.030852193] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054815.030968233] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054816.030894823] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054817.030910965] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054818.031051418] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054819.030907771] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054820.030759681] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054821.031001302] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054822.031043598] [memory_usage_pub]: Publishing: 8.5%
[INFO] [1736054823.030939367] [memory_usage_pub]: Publishing: 8.5%
...
```
- 二つ目の端末
```
[INFO] [1736054915.031510683] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054916.032067852] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054917.031301668] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054918.031673777] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054919.031690321] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054920.031189195] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054921.031777313] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054922.031720671] [memory_listener]: Memory_listener: 8.9%
...
```

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- ©2024 Mitsuno Yuhei
