import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import numpy as np

class StairDetector(Node):
    def __init__(self):
        super().__init__('stair_detector')
        self.sub = self.create_subscription(LaserScan, '/scan', self.callback, 10)
        self.pub = self.create_publisher(Bool, '/stair_detected', 10)
        self.get_logger().info('Stair Detector Node Started')

    def callback(self, msg):
        ranges = np.array(msg.ranges)
        # front arc (−10° to +10°)
        front = np.concatenate((ranges[0:10], ranges[-10:]))
        mean_front = np.nanmean(front)
        mean_next = np.nanmean(ranges[350:370])
        diff = mean_next - mean_front

        detected = diff > 0.3  # threshold for step difference
        self.pub.publish(Bool(data=detected))

        self.get_logger().info(f'Stair detected: {detected}')

def main(args=None):
    rclpy.init(args=args)
    node = StairDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
