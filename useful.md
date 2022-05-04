
# clearing all images and containers

docker rm -vf $(sudo docker ps -aq)

docker rmi -f $(sudo docker images -aq)

