import subprocess

def go_station(x,y,z,w):
     cli_command_str = "ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose \"{pose: {header: {frame_id: 'map'}, pose: {position: {x: 1.0, y: 3.0}, orientation: {z: 0.0, w: 1.0}}}}\""
     cli_command_str = cli_command_str[:129] + str(x) + cli_command_str[132:137] + str(y) + cli_command_str[140:160] + str(z) + cli_command_str[163:168] + str(w) + cli_command_str[171:]
     subprocess.call(cli_command_str,shell=True)
     