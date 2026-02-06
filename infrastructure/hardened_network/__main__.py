import pulumi
import pulumi_aws as aws

# VPC settings with focus in auditory and soverreign
vpc = aws.ec2.Vpc("ghost-sovereign-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags={
        "Name": "ghost-protocol-network",
        "Standard": "DevSecOps",
        "Methodology": "Hardened-by-Design",
        "FinOps-Owner": "Thiago-Nazario"
    })

# Subnet totally private for IA inference
# No direct gateway = Protection against data leak
private_subnet = aws.ec2.Subnet("ai-inference-private-zone",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    map_public_ip_on_launch=False, # Zero-Trust native
    availability_zone="us-east-1a",
    tags={
        "Tier": "Private-Inference",
        "Sovereignty": "High"
    })

# Exporting IDs for external auditory and FinOps tracking
pulumi.export("vpc_id", vpc.id)
pulumi.export("private_subnet_id", private_subnet.id)