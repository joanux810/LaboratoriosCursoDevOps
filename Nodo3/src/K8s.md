# Kubernetes Demo on EKS

[Official Page](https://kubernetes.io/)

[Documentation](https://kubernetes.io/docs/home/)

[Repo](https://github.com/kubernetes/kubernetes)

[Official Training](https://kubernetes.io/training/)

[Important Concepts](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

[Interactive Tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/)

[EKS](https://aws.amazon.com/es/eks/)

## Instructions

1. The tutorial to follow up is:
[K8s Tutorial](https://aws.amazon.com/es/getting-started/hands-on/amazon-eks-with-spot-instances/?trk=gs_card)

```
aws --version
kubectl version
eksctl version
```

2. Deploy an EKS cluster
```
eksctl create cluster --version=1.20 --name=eksdemo --nodes=2 --managed --region=us-east-1 --node-type t2.micro --asg-access

kubectl get nodes
```

3. Add Spot Managed node groups to your EKS cluster

```
eksctl create nodegroup --cluster=eksdemo --region=us-east-1 --managed --spot --name=spot-node-group-2vcpu-8gb --instance-types=m5.large,m5d.large,m4.large,m5a.large,m5ad.large,m5n.large,m5dn.large --nodes-min=2 --nodes-max=5 --asg-access

eksctl create nodegroup --cluster=eksdemo --region=us-east-1 --managed --spot --name=spot-node-group-4vcpu-16gb --instance-types=m5.xlarge,m5d.xlarge,m4.xlarge,m5a.xlarge,m5ad.xlarge,m5n.xlarge,m5dn.xlarge --nodes-min=2 --nodes-max=5 --asg-access

kubectl get nodes --show-labels --selector=eks.amazonaws.com/capacityType=SPOT | grep SPOT
```
4. Deploy the Kubernetes Cluster Autoscaler
   
```
sed -i 's/eksspottutorial/eksspottutorial/g' cluster-autoscaler-autodiscover.yaml

sed -i 's/v1.17.3/v1.20.0/g' cluster-autoscaler-autodiscover.yaml

kubectl apply -f cluster-autoscaler-autodiscover.yaml
```
   
5. Continue the tutorial from here.

sed -i 's/eksdemo/eksspottutorial/g' cluster-autoscaler-autodiscover.yaml

6. Clean-up
We need to specify the region and ensure the Cloudformatio stack is removed. This proces takes few minutes.

```
eksctl delete nodegroup --cluster eksdemo --region us-east-1 --name spot-node-group-2vcpu-8gb

eksctl delete nodegroup --cluster eksdemo --region us-east-1 --name spot-node-group-4vcpu-16gb
```

Removing the cluster

```
eksctl delete cluster --name eksdemo --region us-east-1 
```