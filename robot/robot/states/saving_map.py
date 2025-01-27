import subprocess
import time
from yasmin import Blackboard,State

class SavingMapState(State):
    def __init__(self) -> None:
        super().__init__(["map_saved"])
    
    def execute(self, blackboard: Blackboard) -> str:
        print("map saving state..")
        blackboard.__setitem__("map_saving_started",True)
        time.sleep(3)
        subprocess.call('ros2 run nav2_map_server map_saver_cli -f ./map',shell=True)
        time.sleep(3)
        blackboard.__setitem__("map_saving_started",False)
        return "map_saved"