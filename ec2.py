import boto3
from pprint import pprint

aws_mgmt_console = boto3.session.Session(profile_name='default')
ec2_instance = aws_mgmt_console.client(service_name='ec2')
result = ec2_instance.run_instances(
    ImageId ='0xcv456789',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)

pprint(result)


stop_action = ec2_instance.stop_instances(
    InstanceIds = [
         '0xcv456789'
    ]
)

for stop_each in stop_action:
    print("stopped instances ::", stop_each)