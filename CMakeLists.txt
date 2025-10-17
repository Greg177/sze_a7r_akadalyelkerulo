cmake_minimum_required(VERSION 3.8)
project(sze_a7r_akadalyelkerulo)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

install(
  PROGRAMS
    sze_a7r_akadalyelkerulo/akadalyelkerulo.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME akadalyelkerulo
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
