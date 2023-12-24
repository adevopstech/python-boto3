import boto3

'''
iam = boto3.resource('iam')
for each_user in iam.users.all():
    print(each_user.name)
'''

aws_mgmt_console = boto3.session.Session(profile_name='default')
iam_console = aws_mgmt_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)