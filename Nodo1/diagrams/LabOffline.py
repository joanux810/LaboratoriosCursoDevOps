from diagrams import Cluster, Diagram
from diagrams import Diagram
from diagrams.aws.compute import EC2, EC2AutoScaling
from diagrams.aws.network import VPC, ELB, InternetGateway, PublicSubnet, PrivateSubnet

with Diagram("LabOfflineNetworking"):

    igw = InternetGateway("IGW")

    with Cluster("VPC"):
        vpc = VPC()
        with Cluster("Public Subnet"):
            PublicSubnet()
            webserver = EC2("Apache Web Server")
        with Cluster("Private Subnet"):
            privateSubnet = PrivateSubnet()
            bd = EC2("MySQL Server")

    vpc >> igw
    webserver >> bd

    
