import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():

    # Package Directories
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_gz_PTZ_ctr = get_package_share_directory('gz_ptz_control')
    pkg_ros_gz_bridge = get_package_share_directory('ros_gz_bridge')

    # # Gazebo Sim
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': '-r tsunomi2.sdf'}.items(),
    )

    bridge_pan_cmd = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/world/default/model/PTZCamera/pan_cmd@std_msgs/msg/Float64[gz.msgs.Double',
        ],
        output='screen'
    )

    return LaunchDescription(
        [
            # Nodes and Launches
            gazebo,
            # bridge_pan_cmd,
        ]
    )