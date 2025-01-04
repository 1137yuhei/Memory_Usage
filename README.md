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
```  
`sudo apt install python3-pip`  
`pip install psutil`
```
- リポジトリをクローン
```
`cd ~/ros2_ws/src`
`git clone https://github.com/1137yuhei/Memory_Usage.git`
```
- ディレクトリに移動
```
`cd ~/ros2_ws`
`colon build`
```

###  ノードの実行

- 'binary'スクリプトを実行権限を与える
```
'chmod +x binary'
```
- 'robosys2024'のディレクトリでコマンドを実行する

## 実行方法
```
'echo <数字> | ./binary'
```
## 実行例

- 実行例１
```
$ echo 10 | ./binary
```
- 実行結果１
```
0b1010
```
- 実行例２
```
$ echo -10 | ./binary
```
- 実行結果２
```
-0b1010
```

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- ©2024 Mitsuno Yuhei# ROS2-
