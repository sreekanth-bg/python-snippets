################################################################################
## Author: Sreekanth Govindaiah (sreekanth.govindaiah@accenture.com)          ##
## Created on 21 Mar 2018, Modified on NA                                     ##
## This script will stop an EC2 instance.  The tag 'Name' value should be     ##
## passed as parameter to execute the script along with the keys.             ##
## ex: ./stopEC2-param <ACCESS> <SECRET> <example-instance>                   ##
################################################################################

import sys
import boto3
from boto3.session import Session
from collections import defaultdict 

ACCESS = str(sys.argv[1])
SECRET = str(sys.argv[2])
REGION = 'eu-central-1'
HOST = str(sys.argv[3])

# Passing credentials to boto3 via Session
session = Session(aws_access_key_id=ACCESS,
                  aws_secret_access_key=SECRET,
                  region_name=REGION)

client = session.client('ec2')
ec2 = session.resource('ec2')
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