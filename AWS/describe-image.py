import boto3

client = boto3.client('ec2')

response = client.describe_images(Filters=[{'Name': 'image-id', 'Values': ['ami-925144f2']}])
print(response)

for r in response['Images']:
  for i in r['Instances']:
    print(i['ImageId'], i['Hypervisor'])
#    for b in i['BlockDeviceMappings']:
#      print(b['Ebs']['DeleteOnTermination'])
