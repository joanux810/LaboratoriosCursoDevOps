# More K8s facts

## YAML in Kubernetes

We need to set the following sections within a YAML file that would be consumed by Kubernetes.

```apiVersion```: Describe the Kubernetes version for that specification.

```kind```: Defines the resource we are describing in the YAML file.
This could be 4 types:

- Pod
- Deployment
- ReplicaSet
- Service


```metadata```:
The metadata is data about the object like its name, labels etc.

```spec```:


## ReplicaSet

The replication controller spans across multiples nodes in the cluset. It helps us balance the load accross multiple pods on different nodes as well scale our application when the demand increases.

The replication controller is the older technology that is being replaced by ReplicaSet.


```
kubectl replace -f replicaset-definition.yaml

kubectl scale --replicas=6 -f replicaset-definitions.uml

kubectl scale --replicas=6 replicaset myapp-replicaset

kubectl create -f replicaset-definition.yml

kubectl get replicaset

kubectl delete replicaset myapp-replicaset

kubectl replace -f replicaset-definition.yml

kubectl scale -replicas=6 -f  replicaset-definition.yml

```

## Rollout and versioning

A **rollout** is the process of gradually deploying or upgrading your application containers. When you first create a deployment, it triggers a rollout. A new rollout creates a new Deployment revision. 

## Services
An abstract way to expose an application running on a set of Pods as a network service.
With Kubernetes you don't need to modify your application to use an unfamiliar service discovery mechanism. Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

https://kubernetes.io/docs/concepts/services-networking/service/

