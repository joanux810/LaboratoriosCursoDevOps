# CI/CD Pipeline Demo

## Jenkins

[Official Page](https://www.jenkins.io/)

[Documentation](https://www.jenkins.io/doc/)

[Repo](https://github.com/jenkinsci/jenkins)

[Tutorial](https://aws.amazon.com/es/blogs/opensource/continuous-integration-using-jenkins-and-hashicorp-terraform-on-amazon-eks/)

## Spinnaker

[Official Page](https://spinnaker.io/)

[Documentation](https://spinnaker.io/docs/)

[Repo](https://github.com/spinnaker/spinnaker)

## Terraform

[Official Page](https://www.terraform.io/)

[Documentation](https://www.terraform.io/intro)

[Intro](https://www.terraform.io/intro/index.html)

[Repo](https://github.com/hashicorp/terraform)

### Instructions for Jenkins Server

1. Fork the aws sample [repository](https://github.com/aws-samples/amazon-eks-jenkins-terraform.git)

2. Ensure you create a keypair for ssh purposes on https://console.aws.amazon.com/ec2/ using your account.

3. Open a Cloud9 Instance

4. Check youy AWS account on Cloud9
```
aws configure list
``` 

5. Ensure you have terraform installed
```
terraform --version
``` 
   
6. Create a Jenkins CI server using Terraform by pointing to your repo.

```
git clone https://github.com/aws-samples/amazon-eks-jenkins-terraform.git

cd amazon-eks-jenkins-terraform/terraform/

terraform init

terraform plan
```

7. Place the KeyPair on your Cloud9 instance 
   
8. Update the terraform code to point to your personal keypair; for instance: testJenkins. This file:
   - must be placed on the folder where the terraform files are located 
   - and must exist on the AWS region where the terraform files are pointing to.

9.  Apply the plan to create the resources
    
```
terraform apply -auto-approve
```

10. Open the output address in your browser

```
Apply complete! Resources: 22 added, 0 changed, 0 destroyed.

Outputs:

jenkins_ip_address = "ec2-18-118-207-40.us-east-2.compute.amazonaws.com"
```

http://ec2-34-218-223-213.us-west-2.compute.amazonaws.com:8080

11. Sadly the user data in outdated, so we need to start the service "manually" or modify the install.sh script following [this](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/)

```
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins.io/redhat-stable/jenkins.repo

rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
```
    
> Suggested save the changes in your local repository for future reference

```
git add install_jenkins.sh 

git add terraform.tfvars

sudo git commit -m "updated the jenkins repo, the keypair name and the region that corresponds to the keypair."

git push
```

12. Connect to the jenkins instance via SSH

```
ssh -i "testJenkins.pem" ec2-user@ec2-18-118-207-40.us-east-2.compute.amazonaws.com
```

13. Get the Jenkins password

```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

14. Enter this Administrator password on the Jenkins Console by pasting it into the input box, and click Next. Click Install suggested plugin.

15.  Click Manage Jenkins → Manage Plugins → Available. Choose and install Docker plugin and GitHub Integration Plugin, then restart Jenkins by clicking the Restart Jenkins check box.

16.  Credentials

Docker Hub: Click Credentials → global → Add Credentials, choose Username with password as Kind, enter the Docker Hub username and password and use dockerHubCredentials for ID.

GitHub: Click Credentials → Global → Add Credentials , choose Username with password as Kind,enter the GitHub username and password and use gitHubCredentials for ID.

17. Configure the Jenkins job and [pipeline](https://www.jenkins.io/doc/book/pipeline/)
From the Jenkins console, click New item. Choose Multibranch Pipeline, name it petclinic and click OK.

18. Update the [jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/) to use your docker registry

```
app = docker.build("joanux810/petclinic-spinnaker-jenkins")
```
and
```
sh("docker rmi -f joanux810/petclinic-spinnaker-jenkins:latest || :")
sh("docker rmi -f joanux810/petclinic-spinnaker-jenkins:$SHORT_COMMIT || :")
```

19. Choose GitHub and from the drop-down select the GitHub credentials. Enter the GitHub URL as shown below and click Save to save the Jenkins job.

20. Make sure your jenkins server run a build automatically. You will notice the artifacts about 5 minutes.



### Instructions for Spinnaker CD server

[Tutorial](https://aws.amazon.com/es/blogs/opensource/continuous-delivery-spinnaker-amazon-eks/)
    
1. Using Cloud9, make sure use change the role of the Ec2's Instance to a role with EKS admin priviligies as the EK8's demo in the security tab.

2. Turn off the AWS temporary credentials in your Cloud9 terminal
   
3. Create a AWS Access Key Id in the IAM service.
   
4. Let's prepare the tools on AWS Cloud 9 Terminal by installing AWS CLI, eksctl, kubectl and Halyard.

kubectl

```
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

chmod +x ./kubectl

sudo mv ./kubectl /usr/local/bin/kubectl

kubectl version
```

iam authenticator

```
curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.13.7/2019-06-11/bin/linux/amd64/aws-iam-authenticator

chmod +x ./aws-iam-authenticator

mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator && export PATH=$HOME/bin:$PATH

echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc

aws-iam-authenticator  help
```

Upgrade awscli

```
aws --version
pip install awscli --upgrade --user
```

eksctl

```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv -v /tmp/eksctl /usr/local/bin
```

Halyard

```
curl -O https://raw.githubusercontent.com/spinnaker/halyard/master/install/debian/InstallHalyard.sh

sudo bash InstallHalyard.sh

hal -v
```

5. Create the Production Amazon EKS cluster

```
eksctl create cluster --name=eks-prod --nodes=3 --region=us-east-1 --write-kubeconfig=false
```

6. Create the UAT Amazon EKS cluster

```
eksctl create cluster --name=eks-uat --nodes=3 --region=us-east-1 --write-kubeconfig=false
```

7. Create the Spinnaker Amazon EKS cluster
```
eksctl create cluster --name=eks-spinnaker --nodes=2 --region=us-west-1 --write-kubeconfig=false
```

8. Retrieve Amazon EKS cluster kubectl contexts

```
aws eks update-kubeconfig --name eks-spinnaker --region us-west-1 --alias eks-spinnaker

aws eks update-kubeconfig --name eks-uat --region us-east-1 --alias eks-uat

aws eks update-kubeconfig --name eks-prod --region us-east-1 --alias eks-prod
```
9. Create and configure a Docker registry

```
hal config provider docker-registry enable 

hal config provider docker-registry account add my-docker-registry-march2022 --address index.docker.io --repositories joanux810/petclinic-spinnaker-jenkins --username joanux810 --password
```

10.  Add and configure a GitHub account

```
hal config artifact github enable

hal config artifact github account add joanux810 --username joanux810 --password --token
```

11. Add and configure Kubernetes accounts

Production Amazon EKS account:

```
hal config provider kubernetes enable

kubectl config use-context eks-prod

CONTEXT=$(kubectl config current-context)

kubectl apply --context $CONTEXT -f https://spinnaker.io/downloads/kubernetes/service-account.yml

TOKEN=$(kubectl get secret --context $CONTEXT $(kubectl get serviceaccount spinnaker-service-account --context $CONTEXT -n spinnaker -o jsonpath='{.secrets[0].name}') -n spinnaker -o jsonpath='{.data.token}' | base64 --decode)

kubectl config set-credentials ${CONTEXT}-token-user --token $TOKEN

kubectl config set-context $CONTEXT --user ${CONTEXT}-token-user

hal config provider kubernetes account add eks-prod-apr19 --provider-version v2 --docker-registries my-docker-registry-march2022 --context $CONTEXT
```

UAT Amazon EKS account:

```
kubectl config use-context eks-uat 

CONTEXT=$(kubectl config current-context) 

kubectl apply --context $CONTEXT -f https://spinnaker.io/downloads/kubernetes/service-account.yml

TOKEN=$(kubectl get secret --context $CONTEXT $(kubectl get serviceaccount spinnaker-service-account --context $CONTEXT -n spinnaker -o jsonpath='{.secrets[0].name}') -n spinnaker -o jsonpath='{.data.token}' | base64 --decode)

kubectl config set-credentials ${CONTEXT}-token-user --token $TOKEN

kubectl config set-context $CONTEXT --user ${CONTEXT}-token-user

hal config provider kubernetes account add eks-uat-apr19 --provider-version v2 --docker-registries my-docker-registry-march2022 --context $CONTEXT
```

Spinnaker Amazon EKS account:

```
kubectl config use-context eks-spinnaker 

CONTEXT=$(kubectl config current-context)

kubectl apply --context $CONTEXT -f https://spinnaker.io/downloads/kubernetes/service-account.yml

TOKEN=$(kubectl get secret --context $CONTEXT $(kubectl get serviceaccount spinnaker-service-account --context $CONTEXT -n spinnaker -o jsonpath='{.secrets[0].name}') -n spinnaker -o jsonpath='{.data.token}' | base64 --decode)

kubectl config set-credentials ${CONTEXT}-token-user --token $TOKEN

kubectl config set-context $CONTEXT --user ${CONTEXT}-token-user

hal config provider kubernetes account add eks-spinnaker-apr19 --provider-version v2 --docker-registries my-docker-registry-march2022  --context $CONTEXT
```

12. Enable artifact support

```
hal config features edit --artifacts true
```

13. Configure Spinnaker to install in Kubernetes
    
```
hal config deploy edit --type distributed --account-name eks-spinnaker-apr19
```

14. Configure Spinnaker to use AWS S3

```
export YOUR_ACCESS_KEY_ID=AKIATSGLO6ATLCK6WTBA

hal config storage s3 edit --access-key-id $YOUR_ACCESS_KEY_ID --secret-access-key --region us-west-1

hal config storage edit --type s3
```

 15. Choose the Spinnaker version

```
hal version list

export VERSION=1.15.0

hal config version edit --version $VERSION

hal deploy apply

```
16. Verify the Spinnaker installation

```
kubectl -n spinnaker get svc
```

17. Expose Spinnaker using Elastic Loadbalancer

```
export NAMESPACE=spinnaker

kubectl -n ${NAMESPACE} expose service spin-gate --type LoadBalancer --port 80 --target-port 8084 --name spin-gate-public 

kubectl -n ${NAMESPACE} expose service spin-deck --type LoadBalancer --port 80 --target-port 9000 --name spin-deck-public  

export API_URL=$(kubectl -n $NAMESPACE get svc spin-gate-public -o jsonpath='{.status.loadBalancer.ingress[0].hostname}') 

export UI_URL=$(kubectl -n $NAMESPACE get svc spin-deck-public -o jsonpath='{.status.loadBalancer.ingress[0].hostname}') 

hal config security api edit --override-base-url http://${API_URL} 

hal config security ui edit --override-base-url http://${UI_URL}

hal deploy apply
```

18. Re-verify the Spinnaker installation
```
kubectl -n spinnaker get svc
```

19. Log in to Spinnaker console

20. Create the UAT and Prod Application and Pipelines.


### Cleanup

```
eksctl delete cluster --name=eks-uat --region=us-east-1

eksctl delete cluster --name=eks-prod --region=us-east-1

eksctl delete cluster --name=eks-spinnaker --region=us-east-1
```


