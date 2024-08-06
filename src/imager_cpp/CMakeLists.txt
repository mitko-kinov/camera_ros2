cmake_minimum_required(VERSION 3.8)
project(imager_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(OpenCV REQUIRED)

add_executable(usb_imager src/usb_imager.cpp)
ament_target_dependencies(usb_imager rclcpp sensor_msgs cv_bridge OpenCV)

install(TARGETS
  usb_imager
  DESTINATION lib/${PROJECT_NAME})

ament_package()
