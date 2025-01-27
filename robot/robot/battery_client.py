import sys
from robot_interfaces.srv import Battery
import rclpy
from rclpy.node import Node


class BatteryClient(Node):
    def __init__(self):
        super().__init__("battery_client")
        self.client = self.create_client(Battery,"battery")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("battery service not available, waiting again..")
        

    def send_request(self,body):
        req = Battery.Request()
        req.body = body
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self,future)
        return future.result()
    
def main(args=None):
    rclpy.init(args=args)
    
    battery_client = BatteryClient()

    response = battery_client.send_request(sys.argv[1])

    print(response.result)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()