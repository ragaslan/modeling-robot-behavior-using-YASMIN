# Robot behavior modeling by using state machines

## About project

This project aimed to model robot behaviors by using state machine. YASMIN (yet another state machine) is used as the state machine.


## Setup Steps (for Ubuntu 22.04 )

### install ROS2 Humble

First of all install ros2 to your computer.

Check this web site for details: https://docs.ros.org/en/humble/Installation.html

```bash
# set locale

locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

```

```bash
# setup sources

sudo apt install software-properties-common
sudo add-apt-repository universe

# add ROS2 GPG key with apt
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# add the repository to your sources list
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

```

```bash
# install ros2 packages

sudo apt update
sudo apt upgrade

sudo apt install ros-humble-desktop
sudo apt install ros-humble-ros-base
sudo apt install ros-dev-tools

```

### source ROS2 environment

```bash
# sourcing the setup script

# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh

source /opt/ros/humble/setup.bash

```


### create workspace and src folder

First, go to directory where you want to create your workspace.

Then run these commands:

```bash
mkdir -p ros2_ws/src
cd /ros2_ws/src
```

### clone project

Ensure you’re still in the ros2_ws/src directory before you clone.

```bash
git clone https://github.com/ragaslan/modeling-robot-behavior-using-YASMIN .
```


### resolve dependencies 
From the root of your workspace (ros2_ws), run the following command:

```bash
# get rosdep if you do not have
sudo apt-get install python3-rosdep 
```

```bash
# if your rosdep installation has not been initialized yet. Run: 
sudo rosdep init
rosdep update
```

```bash
# cd if you're still in the "src" directory
cd .. # if you are still in the "src" directory otherwise it is not necessary
rosdep install -i --from-path src --rosdistro humble -y
```

### build workspace with colcon

First, install colcon if does not exist

```bash
# install colcon if does not exist

sudo apt install python3-colcon-common-extensions

```

From the root of your workspace (ros2_ws), you can now build your packages using the command:

```bash
colcon build
```

And you will see that colcon has created new directories:

```bash
ls
```
```
build  install  log  src
```

### source the overlay

First, open new terminal. In the new terminal, source your main ROS 2 environment as the “underlay”, so you can build the overlay “on top of” it:


Source main ROS2 environment

```bash
source /opt/ros/humble/setup.bash
```

Go to your workspace directory

```bash
cd /ros2_ws
```

Source your overlay

```bash
source install/local_setup.bash
```

this is necessary for gazebo

```bash
source /usr/share/gazebo/setup.sh
```

# set key environment variables

```bash
export ROS_DOMAIN_ID=30
export TURTLEBOT3_MODEL=burger 
```

# set burger model parameter
If you get error when you start navigation, you should set some parameters in the burger yaml file

Check this link: https://github.com/turtlebot/turtlebot4/issues/392

```bash
sudo nano /opt/ros/humble/share/turtlebot3_navigation2/param/burger.yaml

# in the yaml file, change the robot_model_type in the line 29;

# from:
# robot_model_type: "differential"

# change that line to :
# robot_model_type: "nav2_amcl::DifferentialMotionModel"
```


### run
Now you can run the package.

```bash
ros2 run robot robot_node
```