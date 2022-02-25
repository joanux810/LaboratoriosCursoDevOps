# DEMO AWS S3 WITH THE AWS CLI

## Basic Frontend

Follow the instructions of Module 1 located at :
[Modern App with Java](https://github.com/aws-samples/aws-modern-application-workshop/tree/java)


The name of the bucket in this tutorial is: mythicalfrontend220223jrc

```
git clone -b java https://github.com/aws-samples/aws-modern-application-workshop.git


aws s3 mb s3://mythicalfrontend220223jrc

aws s3 ls s3://mythicalfrontend220223jrc

aws s3 cp ~/environment/aws-modern-application-workshop/module-1/web/index.html s3://mythicalfrontend220223jrc/index.html


curl -I "https://myticalfrontend220223.s3.us-east-1.amazonaws.com/index.html"

aws s3api put-bucket-policy --bucket mythicalfrontend220223jrc --policy file://~/environment/aws-modern-application-workshop/module-1/aws-cli/website-bucket-policy.json

curl -I "https://mythicalfrontend220223jrc.s3.us-east-1.amazonaws.com/index.html"

aws s3 website s3://mythicalfrontend220223jrc --index-document index.html

http://mythicalfrontend220223jrc.s3-website-us-east-1.amazonaws.com


curl -I http://mythicalfrontend220223jrc.s3-website-us-east-1.amazonaws.com
```

