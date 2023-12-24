import boto3
import logging
from botocore.exceptions import ClientError


# Create bucket
def create_bucket(bucket_name, region='us-east1'):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')

###########################################################################################

# call s3 resource
s3 = boto3.resource('s3')

# print bucket name
for bucket_name in s3.buckets.all():
    print("Bucket name :: ", bucket_name)

# Upload a new file
with open('test.jpg', 'rb') as data:
    s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)