#!/bin/sh
docker run --name $1 -p $1:12348 my_ser2 $2 &
