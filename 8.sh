#!/bin/bash

docker run --name $1 -p $1:12747 my_ser6 $2 &
