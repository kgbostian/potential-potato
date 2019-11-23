# To run the bazel container. Still not sure how to use it. It does have clang.
docker run -it --entrypoint=/bin/bash l.gcr.io/google/bazel:latest



Installing Gtest:
sudo pacman -S gtest
cd /usr/src/gtest
sudo cmake CMakeLists.txt
sudo make
sudo cp *.a /usr/lig
