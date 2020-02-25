################################################################################
## Author: Sreekanth Govindaiah (sreekanth.bg@gmail.com)                      ##
## Created on 19 Apr 2018, Modified on NA                                     ##
## Script to create EC2 instance along with attributes                        ##
################################################################################


import boto3
ec2 = boto3.resource('ec2',region_name='eu-central-1')
tag_purpose_test = {"Key": "Name", "Value": "SBG-Test2s"}
def createInstance():
    instance = ec2.create_instances(ImageId='ami-5055cd3f',
                     InstanceType='t2.micro',
                     MinCount=1, MaxCount=1,
                     #SecurityGroupIds=['sg-34c3ec5f'],
                     KeyName='Ubuntu-12Jan',
                     IamInstanceProfile={'Name': 'DBPOC-EC2-Test'},
                     NetworkInterfaces=[
                        {
                            'DeviceIndex': 0,
                            #'SubnetId' : 'subnet-40bda828',
                            #'Groups': ['sg-34c3ec5f'],
                            'AssociatePublicIpAddress': True            
                        }],
                     TagSpecifications=[{'ResourceType': 'instance',
                                            'Tags': [tag_purpose_test]}])[0]
    # return response
    return instance.instance_id

print(createInstance())


