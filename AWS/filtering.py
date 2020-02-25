################################################################################
## Author: Sreekanth Govindaiah (sreekanth.govindaiah@accenture.com)          ##
## Created on 21 Mar 2018, Modified on NA                                     ##
## This script will first filter the available EC2 instances based on defined ##
## criteria. Then the selected EC2 attributes are displayed for the filtered  ##
## instances.                                                                 ##
################################################################################

import boto3
import datetime
from collections import defaultdict
#from dateutil.parser import *

#define client connection
#client = boto3.client('ec2')

#define resources connection
ec2 = boto3.resource('ec2')

# get instances with filter of running
running_instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# get instances with filter of running + with tag `Exempt`
filter_instances = [i for i in ec2.instances.filter(
    Filters=[{'Name':'tag:Exempt', 'Values':['Yes']}])]

# make a list of filtered instances IDs `[i.id for i in filter_instances]`
# Filter from running instances the instances that are not in the filtered list
display_instances = [disp for disp in running_instances if disp.id not in [i.id for i in filter_instances]]

ec2info = defaultdict()

for instance in display_instances: 
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
        'Up Time': uptime
        } 
attributes = ['Name', 'Type', 'Up Time'] 
for instance_id, instance in ec2info.items():
    print("=====================================")
    for key in attributes:
        print(" {0: <11}: {1}".format(key, instance[key])) 
print("=====================================")