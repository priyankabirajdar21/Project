#!/bin/bash

docker run --name $1 -p $1:12547 my_ser3 $2 &
