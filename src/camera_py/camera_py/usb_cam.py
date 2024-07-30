#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class CameraNode(Node):
    def __init__(self):
        super().__init__("usbcam_node")
        self.publisher_ = self.create_publisher(Image, "usbcam_image", 1)
        self.timer_ = self.create_timer(0.001, self.callback_camera)
        
        self.declare_parameter("camera_slot", 0)
        self.camera_slot_ = self.get_parameter("camera_slot").value
        
        self.cap = cv2.VideoCapture(self.camera_slot_)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 60)
        
        self.bridge = CvBridge()
        
    
    def callback_camera(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_.publish(msg)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
    