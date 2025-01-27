from yasmin import Blackboard,State
import subprocess
import time

class GazeboWorldState(State):
    def __init__(self) -> None:
        super().__init__(["gazebo_started"])
        
    def execute(self, blackboard: Blackboard) -> str:
        print("Loading Gazebo world...")
        
        gazeboWorldProcess = subprocess.Popen(["ros2", "launch", "turtlebot3_gazebo", "turtlebot3_house.launch.py"])
        #gazeboWorldProcess = subprocess.Popen(["ros2", "launch", "turtlebot3_gazebo", "turtlebot3_world.launch.py"])
        time.sleep(8)
        blackboard.__setitem__("gazebo_world_pid",gazeboWorldProcess.pid)
        return "gazebo_started"
