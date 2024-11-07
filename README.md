How to run package: <br/>
source /opt/ros/humble/setup.bash<br/>
export WEBOTS_HOME=/usr/local/webots<br/>
source install/local_setup.bash<br/>
colcon build<br/>
ros2 launch outdoorworld f23_robotics_1_launch.py<br/>
<br/>
Change luminosity to 0 in TexturedBackgroundLight proto to model night time, or change it to 1 for day time

![Screenshot from 2024-11-04 16-35-13](https://github.com/user-attachments/assets/2b635f95-b16a-4d1b-892c-6631a1602676)
