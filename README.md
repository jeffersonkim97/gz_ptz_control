# Dependencies:

ros_gz_bridge
- https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_bridge


# Execution
1. Navigate to worlds folder
   - `cd ~/gz_ptz_control/worlds`
2. Open tsunomi2 world
   - `gz sim tsunomi2.sdf -r`
3. Execute ros2 bridge
   - ros2 bridge for target position
     - `ros2 run ros_gz_bridge parameter_bridge /model/target/pose@geometry_msgs/msg/Pose@gz.msgs.Pose`
   - ros2 bridge for /pan_cmd
     - `ros2 run ros_gz_bridge parameter_bridge /pan_cmd@std_msgs/msg/Float64@gz.msgs.Double`
   - ros2 bridge for image
     - `ros2 run ros_gz_bridge parameter_bridge /camera_x1@sensor_msgs/msg/Image@gz.msgs.Image`
4. Execute tracking script
   - `cd ~/gz_ptz_control/gz_ptz_control`
   - `./pub_sub.py`
5. Execution robot motion for tracking
   - `gz topic -t "/cmd_vel" -m gz.msgs.Twist -p "linear: {x: 0.5}, angular: {z: 0.1}"`
