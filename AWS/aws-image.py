################################################################################
## Author: Sreekanth Govindaiah (sreekanth.bg@gmail.com)                      ##
## Created on 21 Mar 2018, Modified on NA                                     ##
## Script to display description of AMI. Ex: ./aws-image.py SBG-Test1         ##
################################################################################

import boto3
import sys

NAME = str(sys.argv[1])

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
filters = [{
         'Name': 'tag:Name',
         'Values': ['%s' %(NAME)]
            }]
reservations = client.describe_instances(Filters=filters)
#reservations = ec2.describe_instances(Filters=[{'Name': 'InstanceId', 'Values': ['i-04c75e03817996c75']}])
#print(reservations)
for r in reservations['Reservations']:
  for i in r['Instances']:
    image_id = i['ImageId']

image = ec2.Image(image_id)
print(image.description)