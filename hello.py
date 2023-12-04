import boto3
ec2=boto3.resource ('ec2')
regions = ec2.describe_regions('us-east-1')
print(regions)
print(regions)
instance=ec2.create_instances (
    ImageId='ami-063f64fd624326307',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print(instance[0].id)
