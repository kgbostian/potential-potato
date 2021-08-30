cmake_minimum_required(VERSION 3.10)
project(CppApp)
set(CMAKE_BUILD_TYPE Debug)
include_directories(
	${PROJECT_SOURCE_DIR}/include
	${PROJECT_SOURCE_DIR}/src
)

# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
SET(CMAKE_CXX_FLAGS "-g -O0 -Wall -fprofile-arcs -ftest-coverage")
SET(CMAKE_C_FLAGS "-g -O0 -Wall -W -fprofile-arcs -ftest-coverage")
SET(CMAKE_EXE_LINKER_FLAGS "-fprofile-arcs -ftest-coverage")
# Link runTests with what we want to test and the GTest and pthread library
add_executable(allTests test/AllTests.cpp src/Song.cpp src/Album.cpp src/Artist.cpp)
target_link_libraries(allTests ${GTEST_LIBRARIES} pthread gtest_main gcov)
#add_executable(testArtist test/test_artist.cpp)
#target_link_libraries(testAlbum ${GTEST_LIBRARIES} pthread gtest_main)
