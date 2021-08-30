# syntax=docker/dockerfile:1
FROM ubuntu:18.04
ENV TZ=America/Denver
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./cppOpenMicNight /app
CMD ls /app
RUN apt-get -y update
RUN apt-get -y install cmake
RUN apt-get -y install libgtest-dev
RUN apt-get -y install git gcc g++
CMD cd /usr/src/gtest && cmake CMakeLists.txt && make install
CMD cd /app/build && cmake .. && make && ./allTests
