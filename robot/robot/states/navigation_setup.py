from yasmin import State
import subprocess
import time
from nav2_simple_commander.robot_navigator import BasicNavigator
from robot.my_utils.navigation import create_pose
from math import pi
class NavigationSetupState(State):
    def __init__(self):
        super().__init__(["nav2_started"])
        self.nav = BasicNavigator("setup_nav")
        
    def execute(self, blackboard):
        
        navigationSetupProcess = subprocess.Popen(["ros2","launch","turtlebot3_navigation2","navigation2.launch.py","use_sim_time:=True","map:=/home/agaslan/yasmin_ws/map.yaml"])
        
        blackboard.__setitem__("navigation_setup_pid",navigationSetupProcess.pid) 
        time.sleep(3)

        pose = create_pose(self.nav,0.0,0.0,0.0)
        self.nav.setInitialPose(pose)
        
        # wait for nav2 
        self.nav.waitUntilNav2Active()
        
        # rotate robot by using nav2_simple_commander

        self.nav.spin(2 * pi)
        
        while not self.nav.isTaskComplete():
            pass
        
        

        self.nav.destroy_node()
        return "nav2_started"
