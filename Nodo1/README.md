# Node 1 Networking Lab on AWS

## Demo VPC (Networking on AWS)

**Objective**

Provide the infrastructure for a "Hello world" sample application.
The architecture must be high availaible in 3 AZs (Availability Zones)

**Description**

In this demo you will be provide the infraestructure to serve a sample hello world application by creating the following cloud elements.

- VPC  (Virtual Private Cloud)
  - Containing two subnets
  - One public subnet
  - One private subnet
  - One IGW (Internet Gateway) connected to public subnet, allowing Internet to the VPC via RT (Routing Table)

- EC2 Instance containing 
  - nodeJS
  - the sample hello application 

- AMI (Amazon Machine Image) 
  - based in the EC2 Instance
  - Snapshot will be required for this purpose
  
- Application Load Balancer 
  - connected to the EC2 Instance via
  TG (Target group) 
  - Create a SG (Security Group) listenig port 80 via http

- AutoScaling group 
  -  connected to the LB
  -  connected to the TG
  -  Minimum capacity of 2
  -  Desired capacity of 3, 
  -  Max capacity of 10
  
## Steps

Create the following elements in your AWS Console

### VPC  (Virtual Private Cloud)

1. Make sure you are in region us-east1
2. Name the VPC to DemoNetworking
3. Set IPv4 CIDR block(Classless Inter-Domain Routing)  to manual input
4. Set IPv4 CIDR to 10.0.0.0/16
5. 10.0.0.0/24 private range CIDR
6. 10.0.0.34 private host 
7. 10.0.1.0/24 public range CIDR
8. 10.0.1.12 public host
9. Ignore IPv6 and Tenancy sections.
10. Set tag Env = Dev
11. Create the VPC

### Private Subnet

1. Open Subnets
2. Create Subnet
3. Set VPC ID to "DemoNetworking"
4. Notice how the CIDRs are associated with the VPC
5. Set the name to "PrivateSubnet"
6. Choose the AZ to the first zone us-east-1a
7. Set the private subnet's range to a valid CIDR, this tool could help [CIDR calculator](https://www.ipaddressguide.com/cidr), for instance 10.0.0.0/24
8. If you create an EC2 instance wont be reachable via SSH

### Public Subnet
1. Open Subnets
2. Create Subnet
3. Set VPC ID to "DemoNetworking"
4. Set the name to "PublicSubnet"
5. Choose the AZ to the first zone us-east-1b
6. Set a valid range of CIDR, for instance 10.0.1.0/24
7. If you create an EC2 instance won´t be reachable via SSH

### Internet Gateway
1. Open Internet Gateway on VPC Section
2. Create Internet Gateway
3. Set Name to DemoIGW
4. Attach to VPC
5. Select the VPC used in this class
6. Open "Route Table"
7. Choose the Public Subnet
8. Go to "Route Table"
9. Create route table
10. Set name to routeTableDemo
11. Choose the VPC
12. Create route table
13. Choose the route table after creation
14. Go to subnet association
15. Go to Routes
16. Edit routes
17. Add route
18. Choose Destination Any IP (0.0.0.0/0), Target IGW
19. Save changes
20. Go to Subnet Association
21. Go to Explicit Subnet Association
22. Edit subnet association
23. Choose the public subnet
24. Save association
25. Go to Subnets
26. Choose the public subnet
27. Edit subnet settings
28. Enable Auto-assign IP settings
29. Create an EC2 instance and connect via SSH to test the public association.

### EC2 Instance
1. Create an EC2 instance with Amazon Linux AMI
2. Choose the VPC and Public Subnet of this class
3. Install NVM and Node as the previous lesson
   
   ```
   sudo su

   sudo yum update

   curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

   . ~/.bashrc

   nvm install node
   
   node --version
   ```
4. Install git in your EC2 instance
   
   ```
   yum install git
   git  --version
   ```

5. Clone the [repository](https://github.com/joanux810/LaboratoriosCursoDevOps.git) 
   ```
   git clone https://github.com/joanux810/LaboratoriosCursoDevOps.git
   ```
6. Start server 
   ```
   node /src/serverip.js
   ```
7. In this step we have two options to server the application to production.
   - via Apache/NodeJS
   - via PM2
   Description for both options are below and up to you.
8. If you choose install **Apache**, the installation is running 
   ```
   yum install httpd
   ```
    8.1. Start the service
    ```
    httpd start -f /var/www/html/serverip.js
    ```
    8.2. The port 80 is used for the Apache's default page, so update the code to point to another port; for instance 8080
    ```
    vi Git/LaboratoriosCursoDevOps/Nodo1/src/serverip.js
    ```
    8.3. Edit the configuration rules to redirect to 8080
    ```
    vi /etc/httpd/conf/httpd.conf
    ``` 
    by adding at the end of the document
    ```
    LoadModule proxy_module modules/mod_proxy.so
    LoadModule proxy_http_module modules/mod_proxy_http.so
    ProxyPass /node http://localhost:8080
    ```
   
    8.4. Restart the service
    ```
    service httpd restart
    ```
    8.5. Open the port 8080 in the EC2 instance's Security Group

9.  Create a SG with 
   -  HTTP 80
   -  SSH 22
11. Launch the EC2
12. Test the application
13. The following steps describes the PM2 Process
14. Install pm2
    ```
    sudo npm install pm2 -g
    ```
15. Review the current apps running
    ```
    pm2 ls
    ```
16. Start the node application with
    ```
    pm2 start LaboratoriosCursoDevOps/Nodo1/src/serverip.js
    ```
17. Ensure the app is working as expected
18. Enable auto run of the app
    ```
    pm2 startup
    ```
19. Notice the command the is going to return, similar to: 
    ```
    sudo env PATH=$PATH:/home/ec2-user/.nvm/versions/node/v17.4.0/bin /home/ec2-user/.nvm/versions/node/v17.4.0/lib/node_modules/pm2/bin/pm2 startup systemd -u ec2-user --hp /home/ec2-user
    ```
    then, copy and paste in the CLI
20. Proceed to save the configuration with
    ```
    pm2 save
    pm2 startup
    ```
21. Restart your EC2 instance to ensure the app is starting automatically
    ```
    reboot
    ```
22. Check the processes with
    ```
    pm2 list
    ```
23. Check the logs with
    ```
    pm2 logs
    pm2 logs --lines 30
    ```
24. Check the dashboard with
    ```
    pm2 monit
    ```
25. You can stop the app with
    ```
    pm2 stop /var/www/html/serverip.js
    ```

    

   
### Application Load Balancer 
1. Create a new public subnet, for instance 10.0.2.0/24
2. Edit the public route table to add the new public subnet
3. Create a new SG for the LB via http 80
4. Go to Load Balancer
5. Selecte Application Load Balancer
6. Set Name to demoLoadBalancer
7. Set schema to internet-facing
8. Set IP address type to IPV4
9. Select the VPC in this demo
10. Select the public subnet
11. Create a new TG (Target Group)
12. Choose Instances
13. Set the name of the TG
14. Confirm Protocol to HTTP and Port 80
15. Select the VPC in this demo
16. Select Protocol version to HTTP1
17. Leave Advanced health check settings as default values
18. Choose the instances
19. Create the TG
20. Refresh the LB Section
21. Create the Load Balancer
22. Test the Load Balancer


### AMI (Amazon Machine Image)

1. Go to Instances
2. Actions
3. Images and Template
4. Create image
5. Set the name and description ie NodeServer
6. Enable No reboot
7. Review the volume used for the AMI
8. Create image
9. Go to AMIs
10. Select the created image
11. Actions
12. Launch Instance from Image
13. Follow the same process described in the section EC2 Instance
  

    
### AutoScaling group 
1. Go to AutoScaling
2. Go to launch template
3. Select the created AMI in Application and OS Images (AMI)
4. This AMI is located at My AMIs
5. Instance type to t2.micro
6. Select the key pair
7. Wait for it... TBD

### Clean-up

1. Remove the AutoScaling
2. Remove the Load Balancer
3. Remove the EC2 Instances
4. Remove the AMI
5. Remove the snapshot
6. The VPC,IGW, subnets can remain without cost.

## Task offline (Challenge)

**Objective**

Deploy the Sample.php application based on the previous infraestructure.

**Description**

Based on the previous tutorial, add the following elements to your infrastructure:

-  EC2 Instance Web Server
  -  "Deploy" the "Sample.php" application
  -  expose it via port 80 http
  -  in the public subnet
  
- EC2 Instance DataBase
  - Install and configure MySQL Database
  - in the private subnet
  - allow the SG listen from the port 3306 via SQL from the webserver

**Evidence**
1. Test you are able to insert one employee in your application.
2. Send the screenshot of the app running via LMS

**Tutorial**

These resources are useful for your task.

Step 1: [Tutorial: Create an Amazon VPC for use with a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html)

Step 2: [Create an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.CreateDBCluster.html)

Step 3: [Create an EC2 instance and install a web server](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html)

**Evaluation**

| Indicator       | Score  |      
|-----------------|--------------|
| Outstanding     | 1            |
| Satisfactory    |.8           | 
| Medium          | .5           |
| Unsatisfactory  | 0            |