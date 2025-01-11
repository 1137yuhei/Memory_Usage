# SPDX-FileCopyrightText: 2024 Yuhei Mitsuno
# SPDX-License-Identifier: BSD-3-Clause

import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class MemoryUsagePublisher(Node):
    def __init__(self):
        super().__init__("memory_usage_pub")
        self.pub = self.create_publisher(Float64, "memory_usage", 10)
        self.create_timer(1.0, self.publish_memory_usage)
        self.n = 0

    def publish_memory_usage(self):
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        msg = Float64()
        msg.data = memory_usage
        self.pub.publish(msg)
        
def main():
    rclpy.init()
    node = MemoryUsagePublisher()
    rclpy.spin(node)
    rclpy.shutdown()
