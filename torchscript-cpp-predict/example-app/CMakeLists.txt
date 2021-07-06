cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(example-app)

find_package(Torch REQUIRED)
find_package(OpenCV 4.5.1 REQUIRED)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

add_executable(${PROJECT_NAME} sample.cpp)
target_link_libraries( ${PROJECT_NAME} PRIVATE "${TORCH_LIBRARIES}")
target_link_libraries( ${PROJECT_NAME} PRIVATE ${OpenCV_LIBS})
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)

