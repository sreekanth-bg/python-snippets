################################################################################
## Author: Sreekanth Govindaiah (sreekanth.govindaiah@accenture.com)          ##
## Created on 21 Mar 2018, Modified on NA                                     ##
## This script will stop an EC2 instance.  The tag 'Name' value should be    ##
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
        'Values': ['running']
    }]
instances = ec2.instances.filter(Filters=filters)
runningInstances = [instance.id for instance in instances]
if len(runningInstances) > 0:
    stoppingDown = ec2.instances.filter(InstanceIds=runningInstances).stop()