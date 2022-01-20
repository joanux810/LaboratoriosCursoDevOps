# Nodo 0: Linux con AWS Cloud9/NodeJs
**Objetivo**

Levantar una aplicación de NodeJS en AWS

**Descripción**

Levantar de una instancia EC2 usando una imagen de Amazon Linux en AWS y un ambiente de AWS Cloud9 para conectarnos via SSH a la instancia EC2 y con comandos de linux correr una aplicación simple en NodeJs.

**Tutorial**

[Node.js sample for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-nodejs.html)

[Docker sample](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-docker.html)

**Rúbrica de evaluación**

| Indicador        | Ponderación  |      
|------------------|--------------|
| Sobresaliente    | 1            |
| Satisfactoria    |.75           | 
| Medianamente     | .5           |
| No cumple        | 0            |



## Node.js sample for AWS Cloud9

Based on [AWS Cloud9 Node JS](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-nodejs.html#sample-nodejs-prereqs)

```
node --version

sudo yum -y update

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

. ~/.bashrc

nvm install node

node hello.js 5 9
```

## Docker sample for AWS Cloud 9

Based on [Docker sample for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-docker.html)

```
docker --version

sudo service docker start

sudo docker info

sudo touch /tmp/Dockerfile

sudo vi /tmp/Dockerfile

:wq

sudo touch /tmp/authorized_keys

sudo docker build -t cloud9-image:latest /tmp

sudo docker image ls

curl http://169.254.169.254/latest/meta-data/public-ipv4


sudo docker container ls

sudo docker run -d -it --expose 9090 -p 0.0.0.0:9090:22 --name cloud9 cloud9-image:latest

sudo docker container ls

sudo docker exec -it cloud9 bash

sudo docker stop cloud9

sudo docker rm cloud9

sudo docker system prune -a
```


