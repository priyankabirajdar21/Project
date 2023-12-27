#!/bin/bash

docker run --name $1 -p $1:12347 my_ser $2 &
