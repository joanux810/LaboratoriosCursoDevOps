# Docker Demo

[Official Page](https://www.docker.com/)

[Documentation](https://docs.docker.com/get-started/)

[Repo](https://github.com/docker)

[Samples](https://github.com/dockersamples/example-voting-app)


## Instructions

1. Clone the repository

```
git clone https://github.com/dockersamples/example-voting-app.git

cd example-voting-app
```

2. Let's navigate into the source code of each application.

```
cd result
cd vote
cd worker
```

3. We need to deploy the 3 apps. So let's deploy the "voting-app"

```
cd vote
ls
cat Dockerfile
docker build . -t voting-app
docker images
docker run -p 5000:80 voting-app
```

Here is the breakdown of the instructions listed above:

```
docker run -d -p 80:80 docker/getting-started
```

You’ll notice a few flags being used. Here’s some more info on them:

```-d ```: run the container in detached mode (in the background)
```-p 80:80```: map port 80 of the host to port 80 in the container
```docker/getting-started``` - the image to use

4. Test the voting app in your host
http://127.0.0.1:5000/

5. Notice the app fails due to the missing Redis instance

```
docker ps
docker stop CONTAINER_ID
```

6. Let's build a redis container

```
docker run --name=redis redis
docker ps
docker run -p 5000:80 --link redis:redis voting-app
```

7. Let's build the database image

with -d the run is using a silence mode

```
docker run --name=db postgres:9.4
```

or

```
docker run --name=db -e POSTGRES_PASSWORD=USEYOURPSW postgres:9.4
```

to set the postgres master password

8. You must see 3 containers running
   
```
docker ps
docker images
```

9.  Let's build the worker

```
cd worker
docker build . -t worker-app
docker images
docker run --link redis:redis --link db:db worker-app
docker ps
```

10. Finally let's build the result-app

```
cd result
docker build . -t result-app
docker images
docker run -p 5001:80 --link db:db result-app
```

Now let's test the result app
http://127.0.0.1:5001/


1.  Clean up your local system
    
Stop all running containers

```
docker stop $(docker ps -a -q)
```

Removing all containers

```
docker rm $(docker ps -a -q)
```

Removing one specific container

```
docker container rm  CONTAINER_ID
```

Removing all images

```
docker rmi $(docker images -q)
```

Here is a breakdown of docker ```ps -a -q```
docker ps list containers
- a the option to list all containers, even stopped ones. Without this, it defaults to only listing running containers
- q the quiet option to provide only container numeric IDs, rather than a whole table of information about containers

List stopped container

```
docker ps -a
```
