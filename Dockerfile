# syntax=docker/dockerfile:1
FROM ubuntu:18.04
ENV TZ=America/Denver
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./cppOpenMicNight /app
RUN ls /app
RUN apt-get update
RUN apt-get -y install cmake
RUN apt-get -y install libgtest-dev
RUN apt-get -y install git gcc g++
RUN cd /usr/src/gtest && cmake CMakeLists.txt && make install
RUN cd /app/build && cmake .. && make && ./allTests
