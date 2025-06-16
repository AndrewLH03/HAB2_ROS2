from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(cmd=['python3', 'src/clear_i2c.py']),
        Node(package='hab2_ros2', executable='bmp280_node', name='bmp280'),
        Node(package='hab2_ros2', executable='bosch_pressure_node', name='bosch_pressure'),
        Node(package='hab2_ros2', executable='mcp9600_node', name='mcp9600'),
        Node(package='hab2_ros2', executable='gps_node', name='gps'),
        Node(package='hab2_ros2', executable='status_node', name='status'),
        Node(package='hab2_ros2', executable='hab_main_node', name='hab_main'),
    ])
