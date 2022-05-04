# install mysql on server

https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04

sudo apt update

sudo apt install mysql-server

sudo systemctl start mysql.service

      mysql -u root -p
      -- root password

      CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

      GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;

      CREATE USER 'username'@'%' IDENTIFIED BY 'password';

      GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;

      FLUSH PRIVILEGES;

      EXIT;


https://ganeshchandrasekaran.com/dbeaver-public-key-retrieval-is-not-allowed-77eba055bbcd

# Creating Docker Image and Testing it

https://jojozhuang.github.io/architecture/creating-mysql-image-with-docker-file/

https://hevodata.com/learn/docker-mysql/

