# memory_usage
ロボットシステム学授業用
メモリ使用率をトピックから出力するROS2のパッケージ

[![test](https://github.com/1137yuhei/robosys2024/actions/workflows/test.yml/badge.svg)](https://github.com/1137yuhei/robosys2024/actions/workflows/test.yml)

##  ノード概要

###  MemoryUsagePiblisherノード

- ```MemoryUsagePiblisher```:ノードはシステムのメモリの使用率を1秒ごとに計測し、トピックにパブリッシュする

###  listenerノード

- テスト用
- メッセージをサブスクライブして受け取るサブスクライブ

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
  
`sudo apt install python3-pip`  
`pip install psutil`

- リポジトリをクローン

`cd ~/ros2_ws/src`
`git clone https://github.com/1137yuhei/Memory_Usage.git`

- ディレクトリに移動

`cd ~/ros2_ws`
`colon build`

###  ノードの実行

####  一つの端末で実行する方法

  - `ros2 run talk_listen.launch.py`

####  二つの端末で実行する方法

  - 一つ目の端末で以下のコマンドを実行

  `ros2 run mypkg memory_usage_publisher`

  - 二つ目の端末で以下のコマンドを実行

  `ros2 run mypkg listener`

## 実行結果

### 一つの端末で実行した例
```
'echo <数字> | ./binary'
```
### 二つつの端末で実行した例

- 一つ目の端末
```
```
- 二つ目の端末
```
```

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- ©2024 Mitsuno Yuhei# ROS2-
