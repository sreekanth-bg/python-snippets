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
        'Values': ['stopped']
    }]
instances = ec2.instances.filter(Filters=filters)
stoppedInstances = [instance.id for instance in instances]
if len(stoppedInstances) > 0:
    startingUp = ec2.instances.filter(InstanceIds=stoppedInstances).start() 