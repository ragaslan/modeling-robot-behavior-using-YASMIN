from yasmin import Blackboard,State
from robot.my_utils.navigation import create_pose,check_battery
from nav2_simple_commander.robot_navigator import BasicNavigator,TaskResult
#import numpy
import time
#numpy.float = numpy.float64

class NavigationState(State):
    def __init__(self):
        super().__init__(["succeed","failed","canceled","low_battery"])
        self.nav = BasicNavigator()
        
        
    def execute(self, blackboard : Blackboard) -> str:
        # task listener state tarafından görevi alır (blackboard sayesinde)
        
        if check_battery() == 'danger':
            return "low_battery"
        
        if "mission" not in blackboard:
            print("mission could not find")
            return "failed"
        else:
            # görevi yap
            # görev tipine göre görev yap - görev tipi 1 direkt istasyona gitme - görev tipi 2 ise çoklu istasyon gezinimi

            mission : dict = blackboard["mission"]
            mission_type = blackboard["mission"]["type"]

            if(mission_type == 1):
                mission_x = mission["target"]["x"]
                mission_y = mission["target"]["y"]
                mission_z = mission["target"]["z"]
                pose = create_pose(self.nav,float(mission_x),float(mission_y),float(mission_z))
                self.nav.goToPose(pose)

                while not self.nav.isTaskComplete():
                    feedback = self.nav.getFeedback()
                    #print(feedback)
                result = self.nav.getResult()
                if result == TaskResult.SUCCEEDED:
                    return "succeed"
                else:
                    return "failed"
            elif(mission_type == 2 or mission_type == 3):
                poses = []
                targets = mission["target"]
                for target in targets:
                    target_x = target["x"]
                    target_y = target["y"]
                    target_z = target["z"]
                    pose = create_pose(self.nav,float(target_x),float(target_y),float(target_z))
                    poses.append(pose)

                self.nav.followWaypoints(poses)

                while not self.nav.isTaskComplete():
                    time.sleep(1)
                    if(check_battery() == 'danger'):
                        self.nav.cancelTask()
                        time.sleep(2)
                        return "low_battery"
                    else:
                        pass

                result : TaskResult = self.nav.getResult()

                if result == TaskResult.SUCCEEDED:
                    return "succeed"
                else:
                    return "failed"
            
            

            return "failed"