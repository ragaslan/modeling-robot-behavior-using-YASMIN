from yasmin import Blackboard,State
import time
from nav2_simple_commander.robot_navigator import BasicNavigator,TaskResult
from robot.my_utils.navigation import create_pose
from robot.my_utils.navigation import set_battery
class ChargeState(State):
    def __init__(self):
        super().__init__(["battery_full","charge_fail"])
        self.nav = BasicNavigator("charge_nav")

    def execute(self, blackboard : Blackboard) -> str:
        
        print("\n ********** CHARGE STATE IS STARTED *************** \n")

        # istasyon bilgisini oku 0. ya git
        if "charge_station" not in blackboard:
            print("heyyy")
            return "charge_fail"
        
        mission = blackboard["charge_station"]

        mission_x = mission["x"]
        mission_y = mission["y"]
        mission_z = mission["z"]

        charge_pose = create_pose(self.nav,float(mission_x),float(mission_y),float(mission_z))
        
        self.nav.goToPose(charge_pose)

        while not self.nav.isTaskComplete():
            feedback = self.nav.getFeedback()
            #print(feedback)
        
        result = self.nav.getResult()

        if result == TaskResult.SUCCEEDED:
            # burada şarj istasyonuna gitti
            # şarj işlemi simüle
            time.sleep(5)
            set_battery("safe")
            self.nav.destroy_node()
            return "battery_full"
        else:
            # bir olay yok boş durmasın diye verdim ilerde özellik eklenebilir
            print("okeyyy")
            return "charge_fail"
        

       