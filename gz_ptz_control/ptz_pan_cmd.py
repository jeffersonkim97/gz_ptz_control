import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class gzPtzPublisher(Node):
    def __init__(self):
        super().__init__('gz_pan_publisher')
        self.publisher_ = self.create_publisher(JointState, '/actuators', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = JointState()
        msg.position = 3*[1.0]
        msg.velocity = 3*[1.0]
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    gz_ptz_publisher = gzPtzPublisher()

    rclpy.spin(gz_ptz_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gz_ptz_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
