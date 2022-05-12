
# list all containers

docker container ls -a

# show container logs

docker logs 43d3dd7e8efc

# delete all images and containers

sudo docker rm -vf $(sudo docker ps -aq)

docker rmi -f $(sudo docker images -aq)

# dockerfile

https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

