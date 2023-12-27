#!/bin/bash

docker run --name $1 -p $1:12647 my_ser4 $2 &
