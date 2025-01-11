#!/bin/bash
# SPDX-FileCopyrightText: 2024 Yuhei Mitsuno
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

timeout 10 ros2 launch memory_usage talk_listen.launch.py > /tmp/memory_usage.log

cat /tmp/memory_usage.log  |
grep -m 1 "memory_listener"
