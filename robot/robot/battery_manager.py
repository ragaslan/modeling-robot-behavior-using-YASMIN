import rclpy
from rclpy.node import Node
from robot_interfaces.srv import Battery

class BatteryManager(Node):
    def __init__(self):
        super().__init__("battery_manager")
        self.batteryLevel = "safe"
        self.battery = self.create_service(
            Battery,
            "battery",
            self.service_callback
        )

    def service_callback(self,request,response):
        if(request.body == ""):
            response.result = self.batteryLevel
        else:
            self.batteryLevel = request.body
            response.result = request.body

        return response


def main(args=None):

    rclpy.init(args=args)

    battery_manager = BatteryManager()

    rclpy.spin(battery_manager)
    
    rclpy.shutdown()