# syntax=docker/dockerfile:1
FROM alpine:latest
ENV TZ=America/Denver
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#COPY ./cppOpenMicNight /app
RUN apk add --no-cache bash
RUN apk add --no-cache cmake make
RUN apk add --no-cache gtest-dev
RUN apk add --no-cache git gcc g++
#RUN cd /usr/src/gtest && cmake CMakeLists.txt && make install
RUN mkdir /app && cd /app \
    && git clone https://github.com/kgbostian/potential-potato.git \
    && cd potential-potato \
    && cd cppOpenMicNight \
    && mkdir build \
    && cd build 
#    && cmake .. \
#    && make \
#    && ./allTests
