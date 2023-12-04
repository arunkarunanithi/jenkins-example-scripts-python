import boto3
from botocore.config import Config

my_config = Config(
    region_name='us-east-2',
    signature_version='v4'
    )

client = boto3.client('kinesis', config=my_config)

ec2=boto3.resource ('ec2')
instance=ec2.create_instances (
    ImageId='ami-063f64fd624326307',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print(instance[0].id)
