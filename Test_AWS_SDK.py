# Try to connect to the IAM user configured and list available ec2 instances
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html

import boto3

#### List ec2 in all region
client = boto3.client('ec2')
ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
for region in ec2_regions:
    conn = boto3.resource('ec2',region_name=region)
    instances = conn.instances.filter()
    for instance in instances:
        if instance.state["Name"] == "running":
            print (instance.id, instance.instance_type, region)


###### List ec2 only in default region.
ec2 = boto3.resource("ec2")
 for instance in ec2.instances.all():
     print(
         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
     )



