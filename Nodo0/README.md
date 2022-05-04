# Nodo 0: Linux con AWS Cloud9/NodeJs
**Objetivo**

Levantar una aplicación de NodeJS en AWS

**Descripción**

Levantar de una instancia de AWS EC2 usando una imagen de Amazon Linux para correr una aplicación simple en NodeJS, conectando via ssh desde nuestro local.


**Tutorial**
[Node.js sample for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-nodejs.html)

[Docker sample](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-docker.html)

**Entregable**

Screenshot de bash corriendo dentro de una EC2, y conectado via SSH de manera local basado en el Tutorial de Docker Sample.


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
sudo chmod 400 keypar2022.pem

ssh -i "keypar2022.pem" ec2-user@ec2-44-193-212-63.compute-1.amazonaws.com

node --version

curl -sL https://rpm.nodesource.com/setup_16.x | sudo bash -

sudo yum install -y nodejs

node --version  

```

## Docker sample for AWS Cloud 9

Based on [Docker sample for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-docker.html)

```
docker --version

sudo yum install -y docker

sudo service docker start

sudo docker info

sudo touch /tmp/Dockerfile

sudo vi /tmp/authorized_keys

i

:wq

sudo touch /tmp/authorized_keys

sudo docker build -t cloud9-image:latest /tmp

sudo docker image ls

sudo docker container ls

sudo docker run -d -it --expose 9090 -p 0.0.0.0:9090:22 --name cloud9 amazonlinux:latest

sudo docker container ls

sudo docker exec -it cloud9 bash

node --version

sudo docker stop cloud9

sudo docker container ls

sudo docker rm cloud9

sudo docker container ls


sudo docker system prune -a
```


