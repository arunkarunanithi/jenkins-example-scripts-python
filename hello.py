import boto3
ec2=boto3.resource ('ec2')
AWS_DEFAULT_REGION = ec2.describe_regions('us-east-2')
print(regions)
instance=ec2.create_instances (
    ImageId='ami-063f64fd624326307',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print(instance[0].id)
