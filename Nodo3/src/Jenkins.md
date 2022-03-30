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
   
8. Update the terraform code to point to your personal keypair; for instance: testJenkins on the 

9. Apply the plan to create the resources
    
```
terraform apply -auto-approve
```

10. Open the output address in your browser

```
Apply complete! Resources: 22 added, 0 changed, 0 destroyed.

Outputs:

jenkins_ip_address = "ec2-3-145-108-112.us-east-2.compute.amazonaws.com"
```