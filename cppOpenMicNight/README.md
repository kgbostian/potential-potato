# To run the bazel container. Still not sure how to use it. It does have clang.
docker run -it --entrypoint=/bin/bash l.gcr.io/google/bazel:latest



Installing Gtest:
sudo pacman -S gtest
cd /usr/src/gtest
sudo cmake CMakeLists.txt
sudo make
sudo cp *.a /usr/lig

Installing valgrind:
sudo pacman -S valgrind

To get coverage reports.
- make the project (instructions below)
cd build
gcov *.gc* -km

To test for memory leaks with valgrind:
valgrind --tool=memcheck -s ./allTests

To compile and run the simple program.
mkdir build && cd build
cmake ..
make
./allTests
