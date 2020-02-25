################################################################################
## Author: Sreekanth Govindaiah (sreekanth.bg@gmail.com)                      ##
## Created on 19 Apr 2018, Modified on NA                                     ##
## Script to create EC2 instance along with attributes                        ##
################################################################################


import boto3
import time

ec2 = boto3.resource('ec2',region_name='us-west-1')
response = ec2.create_instances(ImageId='ami-925144f2',
                     InstanceType='t2.micro',
                     MinCount=1, MaxCount=1,
                     KeyName='DevOps-Ubuntu',
                     IamInstanceProfile={'Name': 'DevOps-S3-EC2'},
                     NetworkInterfaces=[
                        {
                            'DeviceIndex': 0,
                            'SubnetId' : 'subnet-534b6b34',
                            'Groups': ['sg-3b1bff43'],
                            'AssociatePublicIpAddress': True            
                        }])
instance_id = response[0].instance_id
image_id = response[0].image_id
print(instance_id)
print(image_id)
response = ec2.create_tags(
    Resources=[
        instance_id,
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'SBG-Test2'
        },
        {
            'Key': 'Owner',
            'Value': 'sreekanth.govindaiah@accenture.com'
        },
    ]
)
image = ec2.Image(image_id)
print(image.description)