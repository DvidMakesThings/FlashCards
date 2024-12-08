#!/bin/bash
cd $(dirname "$0")
LOC=$(pwd)
ic=$(docker images | grep -c fdv-apk-builder)
if [ ${ic} -eq 0 ]; then
  docker build -t fdv-apk-builder --progress plain  .
fi
docker run -it -u builder -v ${LOC}:/home/builder/source fdv-apk-builder:latest /bin/sh -lc "cd source; buildozer android debug"
