################################################################################
## Author: Sreekanth Govindaiah (sreekanth.bg@gmail.com)                      ##
## Created on 10 Mar 2018, Modified on NA                                     ##
## Script to display parameters of running and tagged EC2 instances           ##
################################################################################

from collections import defaultdict 
import boto3 

client = boto3.client('ec2')
ec2 = boto3.resource('ec2') 
running_instances = ec2.instances.all()
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
attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Instance ID'] 
for instance_id, instance in ec2info.items(): 
    for key in attributes: 
        print("{0: <11}: {1}".format(key, instance[key])) 
    print("-----------------------------------")