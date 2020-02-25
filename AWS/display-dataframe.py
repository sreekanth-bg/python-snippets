#Script to read ec2 instances details as a dataframe and capture it in a file

#Import packages
import boto3
import pandas as pd
from dateutil.parser import *
import datetime

#Initiate empty list
instance_list = []

#Initiate ec2 client session
region = 'us-east-2'
ec2_client = boto3.client('ec2', region)
filename = region + '_' + datetime.datetime.now().strftime("%Y:%m:%d") + '.csv'

#Use describe_instances method to get response, parse response, append to list
response = ec2_client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        key = instance['KeyName']
        lt_datetime = instance['LaunchTime']
        lt_delta = datetime.datetime.now(lt_datetime.tzinfo) - lt_datetime
        uptime = str(lt_delta)
        private_ip = instance['PrivateIpAddress']
        public_ip = instance['PublicIpAddress']
        state = instance['State']['Name']
        subnet = instance['SubnetId']
        vpc = instance['VpcId']
        security_group = instance['SecurityGroups'][0]['GroupName']
        name = instance['Tags'][0]['Value']
    instance_list.append([instance_id, instance_type, key, uptime, private_ip, public_ip, state, vpc, security_group, name])

#Create dataframe from list
columns = ['instance_id', 'instance_type', 'key', 'uptime', 'private_ip', 'public_ip', 'state', 'vpc', 'security_group', 'name']
instance_df = pd.DataFrame(empty_list, columns = columns)
print(instance_df)
print('The output is recorded in the file:', filename)
instance_df.to_csv(filename) 
