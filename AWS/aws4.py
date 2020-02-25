import boto3
from collections import defaultdict 

ec2 = boto3.resource('ec2')
filters=[{ 
   'Name': 'tag:Name',
   'Values': ['SG-Test']
   },
   {
        'Name': 'instance-state-name', 
        'Values': ['stopped']
    }]
instances = ec2.instances.filter(Filters=filters)
stoppedInstances = [instance.id for instance in instances]
if len(stoppedInstances) > 0:
    startingUp = ec2.instances.filter(InstanceIds=stoppedInstances).start()  				