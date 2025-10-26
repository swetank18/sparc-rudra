from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf_path = os.path.expanduser('~/sparc-rudra/ros2/install/sparc_description/share/sparc_description/urdf/sparc.urdf')
    world_path = os.path.expanduser('~/sparc-rudra/ros2/src/rudra_gazebo/worlds/stairs_world.sdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', world_path, '-r'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_sim', 'create', '-name', 'sparc_rover', '-file', urdf_path, '-z', '1.0'],
            output='screen'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('sparc_nav'), 'launch', 'nav2_bringup.launch.py')
            )
        )
    ])
