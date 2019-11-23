cmake_minimum_required(VERSION 2.6)
project(CppApp)
include_directories(
	${PROJECT_SOURCE_DIR}/include
	${PROJECT_SOURCE_DIR}/src
)

# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
 
# Link runTests with what we want to test and the GTest and pthread library
add_executable(runTests test/test_song.cpp)
target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)

