

# build images

docker build -t jupyterhub_ag:0.1 .

# run container

docker run --detach --name=jupyterhub_ag --publish 8000:8000 jupyterhub_ag:0.1

# list all containers

docker container ls -a

# show container logs

docker logs 43d3dd7e8efc

# delete all images and containers

sudo docker rm -vf $(sudo docker ps -aq)

docker rmi -f $(sudo docker images -aq)
