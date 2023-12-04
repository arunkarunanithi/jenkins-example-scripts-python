import boto3
from botocore.config import Config

proxy_definitions = {
    'http': 'http://proxy.amazon.com:6502',
    'https': 'https://proxy.amazon.org:2010'
}

my_config = Config(
    region_name='us-east-2',
    signature_version='v4',
    proxies=proxy_definitions
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
