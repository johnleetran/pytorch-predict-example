FROM ubuntu:18.04
MAINTAINER john tran

#install python3
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get -y install python3.8 python3-pip

#install clang
WORKDIR /tmp
RUN apt-get -y install wget curl unzip 
RUN wget https://apt.llvm.org/llvm.sh
RUN chmod +x llvm.sh
RUN ./llvm.sh 11

#install cmake
WORKDIR /opt
ENV CMAKE_VERSION 3.20.5
RUN curl -OL https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz
RUN apt-get -y install build-essential checkinstall zlib1g-dev libssl-dev
RUN gunzip -c | tar xfv cmake-${CMAKE_VERSION}.tar.gz
WORKDIR /opt/cmake-${CMAKE_VERSION}
RUN ./configure
RUN make -j4
RUN make install

#install opencv
WORKDIR /opt 
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip
RUN unzip opencv.zip 
RUN mkdir -p build
WORKDIR /opt/build
RUN cmake  ../opencv-master
RUN make -j4 && make install

#download latest libtorch
WORKDIR /opt
RUN wget https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-1.8.1%2Bcpu.zip -O libtorch.zip
RUN unzip libtorch.zip
WORKDIR /opt/libtorch

#install pytorch and torchvision
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD . .
