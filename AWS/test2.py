from collections import defaultdict 
import boto3
from dateutil.parser import *
import datetime

client = boto3.client('ec2')
ec2 = boto3.resource('ec2') 
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
attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Instance ID', 'Up Time'] 
for instance_id, instance in ec2info.items(): 
    for key in attributes: 
        print("{0: <11}: {1}".format(key, instance[key])) 
    print("-----------------------------------")