################################################################################
## Author: Sreekanth Govindaiah (sreekanth.bg@gmail.com)                      ##
## Created on 10 Mar 2018, Modified on 21 Mar 2018                            ##
## Script to display parameters of running and tagged EC2 instances           ##
## Enhancement to calculate uptime by using launch time                       ##
################################################################################

from collections import defaultdict 
import boto3
from dateutil.parser import *
import datetime
import sys

client = boto3.client('ec2')
region = 'us-east-1'
#region = 'us-east-2'
#region = 'us-west-2'
#region = 'ap-south-1'
ec2 = boto3.resource('ec2', region) 
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
attributes = ['Name', 'State', 'Type', 'Up Time'] 
for instance_id, instance in ec2info.items(): 
    for key in attributes: 
        print("{0: <11}: {1}".format(key, instance[key])) 
    print("-----------------------------------")


