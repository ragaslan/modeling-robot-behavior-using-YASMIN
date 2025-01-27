import time
import os
import subprocess
import rclpy
from rclpy.node import Node
from yasmin import State, Blackboard, StateMachine
from yasmin_ros.ros_logs import set_ros_loggers
from yasmin_viewer import YasminViewerPub
# import all states
from robot.states.gazebo_world import GazeboWorldState
from robot.states.initial import InitialState
from robot.states.navigation import NavigationState
from robot.states.saving_map import SavingMapState
from robot.states.slam_operation import SlamOperationState
from robot.states.navigation_setup import NavigationSetupState
from robot.states.navigation import NavigationState
from robot.states.create_station import CreateStationState
from robot.states.charge import ChargeState
from robot.states.teleoperation import TeleoperationState
from robot.states.task_listener import TaskListenerState


class RobotNode(Node):
    def __init__(self):
        super().__init__("robot_node")
        # Create a FSM
        print("FSM with Gazebo World Loading Demo")
        self.sm = StateMachine(outcomes=["end"])
        # Add states with transitions
        self.sm.add_state(
            "InitialState",
            InitialState(),
            transitions = {
                "start_gazebo" : "GazeboWorldState",
                "start_slam_operation" : "SlamOperationState",
                "run_teleoperation" : "TeleoperationState",
                "save_map" : "SavingMapState",
                "create_station" : "CreateStationState",
                "start_navigation" : "NavigationSetupState",
                "end" : "end"
            }
        )
        self.sm.add_state(
            "GazeboWorldState",
            GazeboWorldState(),
            transitions= {
                "gazebo_started" : "InitialState"
            }
        )

        self.sm.add_state(
            "SlamOperationState",
            SlamOperationState(),
            transitions = {
                "slam_operation_started" : "InitialState"
            }
        )

        self.sm.add_state(
            "TeleoperationState",
            TeleoperationState(),
            transitions = {
                "teleoperation_started" : "InitialState"
            }
        )

        self.sm.add_state(
            "SavingMapState",
            SavingMapState(),
            transitions = {
                "map_saved" : "InitialState"
            }
        )

        self.sm.add_state(
            "CreateStationState",
            CreateStationState(),
            transitions= {
                "station_created" : "InitialState"
            }
        )
        self.sm.add_state(
            "NavigationSetupState",
            NavigationSetupState(),
            transitions = {
                "nav2_started" : "TaskListenerState"
            }
        )
        self.sm.add_state(
            "TaskListenerState",
            TaskListenerState(),
            transitions = {
                "task_accepted" : "NavigationState"
            }
        )

        self.sm.add_state(
            "NavigationState",
            NavigationState(),
            transitions = {
                "succeed" : "TaskListenerState",
                "failed" : "TaskListenerState",
                "canceled" : "TaskListenerState",
                "low_battery" : "ChargeState"
            }
        )

        self.sm.add_state(
            "ChargeState",
            ChargeState(),
            transitions= {
                "battery_full" : "TaskListenerState",
                "charge_fail" : "TaskListenerState"
            }
        )

        # Publish FSM info
        YasminViewerPub("My_State_Machine", self.sm)
        
        # Execute the FSM
        outcome = self.sm()
        print("FSM finished with outcome:", outcome)
        
# Main function
def main(args=None):
    
    # Initialize ROS 2
    rclpy.init(args=args)
    set_ros_loggers()
    
    node = RobotNode()
    rclpy.spin(node=node)

    # Shutdown ROS 2
    rclpy.shutdown()

if __name__ == "__main__":
    main()



