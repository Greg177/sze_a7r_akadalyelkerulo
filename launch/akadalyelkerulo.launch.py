from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([


        ExecuteProcess(
            cmd=['ros2', 'run', 'turtlesim', 'turtlesim_node'],
            output='screen'
        ),


        ExecuteProcess(
            cmd=['python3', '-m', 'sze_a7r_akadalyelkerulo.sim_sensor_for_turtle'],
            output='screen'
        ),


        ExecuteProcess(
            cmd=['python3', '-m', 'sze_a7r_akadalyelkerulo.controller_node'],
            output='screen'
        ),


        ExecuteProcess(
            cmd=['python3', '-m', 'sze_a7r_akadalyelkerulo.sensor_node'],
            output='screen'
        ),


        ExecuteProcess(
            cmd=['python3', '-m', 'sze_a7r_akadalyelkerulo.akadalyelkerulo'],
            output='screen'
        ),
    ])
