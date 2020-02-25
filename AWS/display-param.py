################################################################################
## Author: Sreekanth Govindaiah (sreekanth.govindaiah@accenture.com)          ##
## Created on 21 Mar 2018, Modified on NA                                     ##
## This script will display an EC2 instance in a region.The AWS secret keys   ##
## is passed as parameter to execute the script.                              ##
## ex: ./display-param <ACCESS> <SECRET>                                      ##
################################################################################

import sys
import boto3
from boto3.session import Session
from collections import defaultdict
from dateutil.parser import *
import datetime

ACCESS = str(sys.argv[1])
SECRET = str(sys.argv[2])
REGION = 'eu-central-1'

# Passing credentials to boto3 via Session
session = Session(aws_access_key_id=ACCESS,
                  aws_secret_access_key=SECRET,
                  region_name=REGION)

client = session.client('ec2')
ec2 = session.resource('ec2')

running_instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
ec2info = defaultdict() 
for instance in running_instances: 
    for tag in instance.tags: 
        if 'Name'in tag['Key']: 
            name = tag['Value']
            lt_datetime = instance.launch_time
            lt_delta = datetime.datetime.now(lt_datetime.tzinfo) - lt_datetime
            uptime = str(lt_delta)
    # Add instance info to a dictionary 
    ec2info[instance.id] = { 
        'Name': name, 
        'Type': instance.instance_type, 
        'State': instance.state['Name'], 
        'Private IP': instance.private_ip_address, 
        'Public IP': instance.public_ip_address, 
        'Instance ID': instance.id,
        'Up Time': uptime
        } 
attributes = ['Name', 'Instance ID', 'Private IP' ] 
for instance_id, instance in ec2info.items(): 
    for key in attributes: 
        print("{0: <11}: {1}".format(key, instance[key])) 
    print("-----------------------------------")