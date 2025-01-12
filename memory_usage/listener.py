# SPDX-FileCopyrightText: 2024 Yuhei Mitsuno
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


rclpy.init()
node = Node("memory_listener")


def cb(msg):
    global node
    node.get_logger().info(f"Memory_listener: {msg.data}%")


def main():
    sub = node.create_subscription(Float64, "memory_usage", cb, 10)
    rclpy.spin(node)
