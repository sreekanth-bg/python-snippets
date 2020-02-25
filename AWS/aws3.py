#!/usr/bin/env   python 
from collections import defaultdict 
import boto3 

client = boto3.client('ec2')
ec2 = boto3.resource('ec2') 
running_instances = ec2.instances.filter(Filters=[{ 
   'Name': 'instance-state-name', 
   'Values': ['running']}]) 
ec2info = defaultdict() 
for instance in running_instances: 
    for tag in instance.tags: 
        if 'Name'in tag['Key']: 
            name = tag['Value'] 
    # Add instance info to a dictionary 
    ec2info[instance.id] = { 
        'Name': name, 
        'Type': instance.instance_type, 
        'State': instance.state['Name'], 
        'Private IP': instance.private_ip_address, 
        'Public IP': instance.public_ip_address, 
        'Instance ID': instance.id 
        }
attributes = ['Name'] 
for instance_id, instance in ec2info.items(): 
    for key in attributes: 
        with open("running.txt", "a") as myfile:
            myfile.write(instance[key]+"\n")
		