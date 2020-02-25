import boto3
import sys
import time
from collections import defaultdict

HOST = str(sys.argv[1])

ec2 = boto3.resource('ec2')
filters1=[{ 
   'Name': 'tag:Name',
   'Values': ['%s' %(HOST)]
   },
   {
        'Name': 'instance-state-name', 
        'Values': ['stopped']
    }]
filters2=[{ 
   'Name': 'tag:Name',
   'Values': ['%s' %(HOST)]
   },
   {
        'Name': 'instance-state-name', 
        'Values': ['running']
    }]
instances = ec2.instances.filter(Filters=filters1)
stoppedInstances = [instance.id for instance in instances]
if len(stoppedInstances) > 0:
    startingUp = ec2.instances.filter(InstanceIds=stoppedInstances).start()
time.sleep(60)
ec2info = defaultdict()
for instance in ec2.instances.filter(Filters=filters2):
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
        'Launch Time': instance.launch_time
        }

attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")
