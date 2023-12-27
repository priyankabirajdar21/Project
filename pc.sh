#!/bin/bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu `lsb_release -cs` test"
sudo apt update
sudo apt install -y docker-ce
sudo docker run hello-world
sudo apt-get update
sudo apt install -y python3-pip
pip3 install xlwt
pip3 install networkx
pip3 install scipy
chmod 755 1.sh
chmod 755 2.sh
chmod 755 3.sh
chmod 755 4.sh
chmod 755 5.sh
chmod 755 6.sh
chmod 755 7.sh
chmod 755 8.sh
chmod 755 9.sh
chmod 755 10.sh
chmod 755 11.sh
chmod 755 12.sh
cd cont1/
sudo docker build -t my_ser .
cd ..
cd cont2/
sudo docker build -t my_ser2 .
cd ..
cd cont3/
sudo docker build -t my_ser3 .
cd ..
cd cont4/
sudo docker build -t my_ser4 .
cd ..
cd cont5/
sudo docker build -t my_ser5 .
cd ..
cd cont6/
sudo docker build -t my_ser6 .
cd ..
cd cont7/
sudo docker build -t my_ser7 .
cd ..
cd cont8/
sudo docker build -t my_ser8 .
cd ..
cd cont9/
sudo docker build -t my_ser9 .
cd ..
cd cont10/
sudo docker build -t my_ser10 .
cd ..
sudo chmod 666 /var/run/docker.sock
