
cmake_minimum_required(VERSION 3.5)
project(projectx)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
set(CMAKE_CXX_FLAGS_RELEASE "-O2")

set(
  SOURCE_FILES
  itf1/test1.cpp
  itf2/test2.cpp
  itf1/pyGw_test1.cpp
  itf2/pyGw_test2.cpp
)
set(
  HEADER_FILES
  itf1/test1.h
  itf2/test2.h
)

find_package(Boost COMPONENTS system filesystem )


add_library(
  ${PROJECT_NAME} SHARED
  ${SOURCE_FILES} 
  ${HEADER_FILES}
)

target_link_libraries(
  ${PROJECT_NAME}
  ${Boost_LIBRARIES}
)