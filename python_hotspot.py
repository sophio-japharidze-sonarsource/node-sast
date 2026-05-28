from aws_cdk import aws_ec2 as ec2

ec2.Instance(
    self,
    "vpc_subnet_public",
    instance_type=nano_t2,
    machine_image=ec2.MachineImage.latest_amazon_linux(),
    vpc=vpc,
    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC) # Sensitive
)
