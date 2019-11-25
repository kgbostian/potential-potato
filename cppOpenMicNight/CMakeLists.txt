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
add_executable(allTests test/AllTests.cpp src/Song.cpp src/Album.cpp)
target_link_libraries(allTests ${GTEST_LIBRARIES} pthread gtest_main)
#add_executable(testAlbum test/test_album.cpp)
#target_link_libraries(testAlbum ${GTEST_LIBRARIES} pthread gtest_main)
