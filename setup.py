from setuptools import setup, find_packages

package_name = 'sze_a7r_akadalyelkerulo'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Szép Gergő Krisztián',
    maintainer_email='szepgergo13@gmail.com',
    description='Egyszerű akadályelkerülő robot ROS2-höz',
    license='GPLv3',
    entry_points={
        'console_scripts': [
            'akadalyelkerulo = sze_a7r_akadalyelkerulo.akadalyelkerulo:main',
            'controller_node = sze_a7r_akadalyelkerulo.controller_node:main',
            'sensor_node = sze_a7r_akadalyelkerulo.sensor_node:main',
            'sim_sensor_for_turtle = sze_a7r_akadalyelkerulo.sim_sensor_for_turtle:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/akadalyelkerulo.launch.py']),
    ],
)
