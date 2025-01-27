import subprocess
import time
from yasmin import Blackboard,State

class SlamOperationState(State):
    def __init__(self) -> None:
        super().__init__(["slam_operation_started"])
    def execute(self, blackboard: Blackboard) -> str:
        
        print("Performing slam operation...")
        time.sleep(4)
        slam_operation_process = subprocess.Popen(["ros2", "launch", "turtlebot3_cartographer", "cartographer.launch.py","use_sim_time:=True"])
        time.sleep(4)
        blackboard.__setitem__("slam_operation_pid",slam_operation_process.pid)
        return "slam_operation_started"
    