cmake_minimum_required(VERSION 3.20)
project(CLI_module C)
set(CMAKE_C_STANDARD 11)
find_package(Python3 COMPONENTS Development REQUIRED)
include_directories(${Python3_INCLUDE_DIRS})

add_library(CLI_module SHARED src/c/module.c src/c/Addition/Add.h src/c/Addition/Add.c src/c/Division/Div.h src/c/Division/Div.c
        src/c/Multiplication/Multi.h src/c/Multiplication/Multi.c src/c/Subtraction/Sub.c src/c/OpHandler/op_handler.h src/c/OpHandler/op_handler.c
        src/c/module.c)
target_link_libraries(CLI_module PRIVATE ${Python3_LIBRARIES})
set_target_properties(CLI_module PROPERTIES SUFFIX ".pyd")
set_target_properties(CLI_module PROPERTIES PREFIX "")
