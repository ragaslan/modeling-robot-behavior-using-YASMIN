import subprocess
import time
from yasmin import Blackboard,State


class TeleoperationState(State):
    def __init__(self) -> None:
        super().__init__(["teleoperation_started"])
    
    def execute(self, blackboard: Blackboard) -> str:
        print("Running teleoperation node...")
        blackboard.__setitem__("teleoperation_started",True)
        time.sleep(3)
        subprocess.call('ros2 run turtlebot3_teleop teleop_keyboard',shell=True)
        time.sleep(3)
        blackboard.__setitem__("teleoperation_started",False)
        return "teleoperation_started"
