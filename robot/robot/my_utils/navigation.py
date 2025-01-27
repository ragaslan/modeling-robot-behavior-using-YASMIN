from nav2_simple_commander.robot_navigator import BasicNavigator
import tf_transformations
from geometry_msgs.msg import PoseStamped
import subprocess

def create_pose(nav : BasicNavigator,pos_x,pos_y,orientation_z):
        q_x,q_y,q_z,q_w = tf_transformations.quaternion_from_euler(0,0,orientation_z)
        poseObj = PoseStamped()
        poseObj.header.frame_id = 'map'
        poseObj.header.stamp = nav.get_clock().now().to_msg()
        
        poseObj.pose.position.x = pos_x
        poseObj.pose.position.y = pos_y
        poseObj.pose.position.z = 0.0

        poseObj.pose.orientation.x = q_x
        poseObj.pose.orientation.y = q_y
        poseObj.pose.orientation.z = q_z
        poseObj.pose.orientation.w = q_w
        return poseObj


def check_battery():
        response = subprocess.getoutput("ros2 run robot battery_client ''")
        return response

def set_battery(target):
        response = subprocess.getoutput(f"ros2 run robot battery_client '{target}'")
        return response