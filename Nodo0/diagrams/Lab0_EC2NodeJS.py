from diagrams import Cluster, Diagram
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import VPC

with Diagram("Lab0_EC2InstanceNodeJS"):
    with Cluster("AWS Public Cloud"):
        with Cluster("Region us-east-1"):
            with Cluster("AZ us-east-1a"):
                with Cluster("VPC"):
                    with Cluster ("Public Subnet"):
                        EC2("NodeJS")
