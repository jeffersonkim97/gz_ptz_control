import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro


def generate_launch_description():

    # Package Directories
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # # Robot state publisher
    # robot_state_publisher = Node(
    #     package='gz_ptz_publisher',
    #     executable='robot_state_publisher',
    #     name='robot_state_publisher',
    #     output='both',
    #     parameters=[robot_description],
    # )

    # # Gazebo Sim
    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
    #     ),
    #     launch_arguments={'gz_args': '-r empty.sdf'}.items(),
    # )

    # # RViz
    # rviz = Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     arguments=['-d', os.path.join(pkg_ros_gz_sim_demos, 'rviz', 'joint_states.rviz')],
    # )

    # Gz - ROS Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            # Clock (IGN -> ROS2)
            # '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            # Joint states (IGN -> ROS2)
            '/world/default/model/PTZCamera/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model',
        ],
        remappings=[
            ('/world/default/model/PTZCamera/joint_state', 'joint_states'),
        ],
        output='screen'
    )

    return LaunchDescription(
        [
            # Nodes and Launches
            # gazebo,
            # spawn,
            bridge,
            # robot_state_publisher,
            # rviz,
        ]
    )