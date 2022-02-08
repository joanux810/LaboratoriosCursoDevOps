from diagrams import Cluster, Diagram
from diagrams import Diagram
from diagrams.aws.compute import EC2, EC2AutoScaling
from diagrams.aws.network import VPC, ELB, InternetGateway, PublicSubnet, PrivateSubnet

with Diagram("DemoVPCNetworking"):

    igw = InternetGateway("IGW")

    
    with Cluster("VPC"):
        vpc = VPC()
        with Cluster("Public SubNet 1"):
            PublicSubnet()
            EC2InstancesTG1 = [EC2("Web Server1"),
                               EC2("Web Server2")]
        with Cluster("Public Subnet 2"):
            PublicSubnet()
            EC2InstancesTG2 = [EC2("Web Server1"),
                               EC2("Web Server2")]
        with Cluster("Private SubNet"):
            privateSubnet = PrivateSubnet()

    vpc >> igw

    autoscaling = EC2AutoScaling("AutoScaling")
    loadBalancer = ELB("Load Balancer")            
   
    loadBalancer >> autoscaling >> EC2InstancesTG1
    loadBalancer >> autoscaling >> EC2InstancesTG2
    
