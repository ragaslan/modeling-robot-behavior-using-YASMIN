from yasmin import Blackboard,State
import subprocess
from subprocess import Popen
import time
from robot.my_utils.kill_process import killProcess
class InitialState(State):
    def __init__(self) -> None:
        super().__init__(["start_gazebo","start_slam_operation","run_teleoperation","save_map","create_station","start_navigation","end"])

        # # run battery server
        subprocess.Popen(["ros2 run robot battery_manager"],shell=True)
        
    def execute(self,blackboard: Blackboard) -> str:
        # burada ana durumda komutlar alarak diğer durumlara geçiş yap
        print("initial state is active")

        

        
        flag = True
        while(flag):
            print("\nSelect Process\n1) Load Gazebo World\n2) Start Slam Operation\n3) Run Teleoperation Node\n4)Save Map\n5)Create Station Point\n6)Navigation Start\nQ)Exit")
            choice = input("Your Choice: ")
            
            if choice == "1":
                if "gazebo_world_pid" in blackboard and blackboard.__getitem__("gazebo_world_pid"):
                    print("\nGazebo World is already started! ")
                else:
                    return "start_gazebo"
            if choice == "2":
                if "slam_operation_pid" in blackboard and blackboard.__getitem__("slam_operation_pid"):
                    print("\nSLAM operation is already started!")
                else:
                    return "start_slam_operation"
            if choice == "3":
                if  "teleoperation_started" in blackboard and blackboard.__getitem__("teleoperation_started"):
                    print("\nTeleoperation is already started! ")
                else:
                    return "run_teleoperation"
            if choice == "4":
                if  "map_saving_started" in blackboard and blackboard.__getitem__("map_saving_started"):
                    print("\nMap saving process is already started! ")
                else:
                    return "save_map"
            if choice == "5":
                if "create_station_started" in blackboard and blackboard.__getitem__("create_station_started"):
                    print("\nCreate Station is already started")
                else:
                    return "create_station"
            if choice == "6":
                if "navigation_setup_pid" in blackboard and blackboard.__getitem__("navigation_setup_pid"):
                    print("\nNavigation is already started")
                else:
                    return "start_navigation"
            if choice == "q" or choice == "Q":
                # çıkış yaparken bazı açık kalabilecek kaynakları kapat pid leri okuyarak örnegin : rviz, gazebo world vs...
                #killProcess(blackboard,"gazebo_world_pid")
                #killProcess(blackboard,"slam_operation_pid")
                return "end"

                        
                