################################################################################
## Author: Sreekanth Govindaiah (sreekanth.govindaiah@accenture.com)          ##
## Created on 21 Mar 2018, Modified on NA                                     ##
## This script will start an EC2 instance.  The tag 'Name' value should be    ##
## passed as parameter to execute the script.                                 ##
## ex: ./startEC2 example-instance                                            ##
################################################################################

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