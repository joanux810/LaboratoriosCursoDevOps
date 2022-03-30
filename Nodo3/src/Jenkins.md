# Jenkins Demo

[Official Page](https://www.jenkins.io/)

[Documentation](https://www.jenkins.io/doc/)

[Repo](https://github.com/jenkinsci/jenkins)

[Tutorial](https://aws.amazon.com/es/blogs/opensource/continuous-integration-using-jenkins-and-hashicorp-terraform-on-amazon-eks/)

# Spinnaker

[Official Page](https://spinnaker.io/)

[Documentation](https://spinnaker.io/docs/)

[Repo](https://github.com/spinnaker/spinnaker)


## Instructions

1. Fork the aws sample [repository](https://github.com/aws-samples/amazon-eks-jenkins-terraform.git)

2. Ensure to have your keypairs for ssh purposes.

3. Open a Cloud9 Instance
   
4. Create a Jenkins CI server using Terraform by pointing to your repo.

```
git clone https://github.com/aws-samples/amazon-eks-jenkins-terraform.git

cd amazon-eks-jenkins-terraform/terraform/

terraform init

terraform plan

terraform apply -auto-approve
```

5. 