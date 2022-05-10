
# mapping github users to system users
https://github.com/jupyterhub/dockerspawner/issues/94

# run container as host user not root
https://jtreminio.com/blog/running-docker-containers-as-current-host-user/

# create volume on host and add to docker container
https://medium.com/@nielssj/docker-volumes-and-file-system-permissions-772c1aee23ca

# commands tun on vm

    sudo su
    cd \
    mkdir data
    mkdir myvolume
    ls -al # list all with permissions
    
# Dockerfile

    # The source image to start with
    FROM ubuntu:latest

    # Create a volume
    VOLUME /myvolume
   
# delete all images

docker rmi -f $(sudo docker images -aq)

# delete all containers

docker rm -vf $(sudo docker ps -aq)

# list all volumes

docker volume ls -qf

# delete all volumes

docker volume rm $(docker volume ls -qf) ## check this?

# create image

sudo docker build -t dockerfile-volumetest .

# run container

sudo docker run -v /data/myvolume:/data/myvolume --name my-dockerfile-test -it dockerfile-volumetest /bin/bash


