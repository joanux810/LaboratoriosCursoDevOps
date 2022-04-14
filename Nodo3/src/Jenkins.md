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

### Instructions

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

20. Install [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) on Cloud9

```
sudo su
sudo curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.22.6/2022-03-09/bin/linux/amd64/kubectl

sudo curl -o kubectl.sha256 https://s3.us-west-2.amazonaws.com/amazon-eks/1.22.6/2022-03-09/bin/linux/amd64/kubectl.sha256

sudo openssl sha1 -sha256 kubectl

sudo chmod +x ./kubectl

sudo mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin

sudo echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc

kubectl version --short --client
```

21. Install EKS and AWS CLI
    
```
sudo curl --silent --location -o "awscliv2.zip" "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"

sudo unzip awscliv2.zip && sudo ./aws/install

aws --version

curl --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv -v /tmp/eksctl /usr/local/bin

export PATH=$PATH:/usr/local/bin/

eksctl version
```

22.  Create the cluster with [EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html)
    
```
eksctl create cluster --name petclinic --version 1.20 --region us-east-1 --nodegroup-name linux-nodes --node-type t2.micro --nodes 2
```

24. Test installation with

```
eksctl version
kubectl get node
kubectl get pod
kubectl get svc
```

25. Install spinnaker service 
```
kubectl get svc -n spinnaker
```

Clean-up
```
 eksctl delete cluster --region=us-east- --name=eksPetclinic
```
