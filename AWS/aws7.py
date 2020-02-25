import boto3
import sys
from collections import defaultdict 

HOST = str(sys.argv[1])

ec2 = boto3.resource('ec2')
filters=[{ 
   'Name': 'tag:Name',
   'Values': ['%s' %(HOST)]
   },
   {
        'Name': 'instance-state-name', 
        'Values': ['running']
    }]
instances = ec2.instances.filter(Filters=filters)
runningInstances = [instance.id for instance in instances]
if len(runningInstances) > 0:
    stoppingDown = ec2.instances.filter(InstanceIds=runningInstances).stop()