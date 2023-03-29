import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    DeclareLaunchArgument,
    OpaqueFunction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):

    depthai_prefix = get_package_share_directory("depthai_ros_driver")
    interbotix_prefix = get_package_share_directory("interbotix_xsarm_moveit")

    interbotix_moveit = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(interbotix_prefix, 'launch',
                         'xsarm_moveit.launch.py')
        ),
        launch_arguments={"robot_model": "vx300s",
                          "hardware_type": "actual"}.items())

    spatial_rgbd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(depthai_prefix, 'launch',
                         'rgbd_pcl.launch.py')
        ),
        launch_arguments={"name": "oak",
                          "parent_frame": "vx300s/ee_arm_link",
                          "cam_pos_z": str(0.1)}.items())
    nodes=[]
    nodes.append(spatial_rgbd)
    nodes.append(interbotix_moveit)
    return nodes


def generate_launch_description():

    return LaunchDescription(
        [
            OpaqueFunction(function=launch_setup),
        ]
    )
