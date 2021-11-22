import boto3
import json
s3 = boto3.client("s3")
bucket_name='pythonexamplebucket'
lifecycle_config = {
    'Rules': [
        {'ID': 'Delete Rule',
         'Filter': {'Prefix': ''},
         'Status': 'Enabled',
         'Expiration': { 'Days':14 }}
    ]}

bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:*"],
                "Resource": ["arn:aws:s3:::pythonexamplebucket/*"],
                "Condition": {
                    "NotIpAddress": {
                       "aws:SourceIp": [
                         "11.11.11.11/32",
                         "22.22.22.22/32"
                       ]
                    }
               }
            }
        ]
    }
policy_string = json.dumps(bucket_policy)
print(policy_string) 
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
           'LocationConstraint': 'eu-west-1'})
s3.put_bucket_policy(Bucket=bucket_name, Policy=policy_string)
s3.put_bucket_lifecycle_configuration(Bucket=bucket_name,
                                              LifecycleConfiguration=lifecycle_config)
