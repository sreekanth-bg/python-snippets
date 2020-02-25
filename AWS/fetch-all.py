################################################################################
## Author: Sreekanth Govindaiah (sreekanth.govindaiah@accenture.com)          ##
## Created on 21 Mar 2018, Modified on NA                                     ##
## This script will list all EC2 instances without any filters                ##
################################################################################

from collections import defaultdict 
import boto3 

client = boto3.client('ec2')
ec2 = boto3.resource('ec2') 
running_instances = ec2.instances.all()
ec2info = defaultdict() 
for instance in running_instances: 
    # Add instance info to a dictionary 
    ec2info[instance.id] = { 
        'Name': instance.tags, 
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