from yasmin import Blackboard,State
import subprocess
import time
from robot.my_utils.kill_process import killProcess

class CreateStationState(State):
    # teleop yaparken o anki robot konumunun istasyon olarak kaydedilmesi için istasyon kaydetme durumuna geçip istasyon oluşturulması
    # initial state kayıt sonrası dönüş
    def __init__(self):
        super().__init__(["station_created"])
    
    def execute(self,blackboard : Blackboard) -> str:
        print("station creating is active")
        blackboard.__setitem__("create_station_started",True)
        # listen /clicked_point topic by starting subscriber program
        clickedPointSubscriberProcess = subprocess.Popen(["ros2","run","robot","clicked_point_subscriber"])

        choice = input("Press Q to exit station creating state")
        while(choice != "Q" and choice != "q"):
            # wait until exit command from cli
            choice = input("Press Q to exit station creating state")
        
        # kill listener process
        clickedPointSubscriberProcess.kill()
        
        # close rviz if is open
        #killProcess(blackboard,"slam_operation_pid")
        killProcess(blackboard,"gazebo_world_pid")
        
        blackboard.__setitem__("create_station_started",False)
        # go back to initial state
        return "station_created"
