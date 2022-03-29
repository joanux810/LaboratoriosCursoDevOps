# Docker Swarm Demo

[Official Page](https://docs.docker.com/engine/swarm/)

[Documentation](https://docs.docker.com/engine/swarm/key-concepts/)

[Repo](https://github.com/docker-archive/classicswarm)


## Instructions

Quick demo for Docker Swarm

1. We are going to follow this [tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)
   
Ensure docker swarm in your system

```
docker swarm init --help
```

2. Verify a host available in your system
   
> The IP address must be assigned to a network interface available to the host operating system. All nodes in the swarm need to connect to the manager at the IP address. 
Because other nodes contact the manager node on its IP address, you should use a fixed IP address.

>You can run ifconfig on Linux or macOS to see a list of the available network interfaces.

>The following ports must be available. On some systems, these ports are open by default.

>TCP port 2377 for cluster management communications
TCP and UDP port 7946 for communication among nodes
UDP port 4789 for overlay network traffic

```
ifconfig
```

We are going to use 127.0.0.1

1. Initialize swarm:

```
docker swarm init --advertise-addr  127.0.0.1
```
If you need to add a worker to the node.

```
docker swarm join --token <token>  127.0.0.1:2377
```

2. Let's add some services with
[create](https://docs.docker.com/engine/reference/commandline/service_create/)
and [update](https://docs.docker.com/engine/reference/commandline/service_update/)
with arguments like [replicas](https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service/)

```
docker service create --replicas 3 --name redis --update-delay 10s redis:3.0.6

docker service update --image redis:3.0.7 redis

docker service create --name my-web  publish published=8080 target=80 --replicas 2 nginx
```

3. Commands to see information about the Docker Nodes.

```
docker info
docker ps
docker node ls
docker service ps
```

4. Clean-up

```
docker service rm redis

docker service rm my-web

docker swarm leave --force
```