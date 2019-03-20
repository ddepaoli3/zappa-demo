#!/usr/bin/env python
import boto3
import string
import random

BUCKET_NAME="zappa-demo-2jps4g"
KEY=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

def random_data():
    more_binary_data = b'Here we have some more data'

    # Method 2: Client.put_object()
    client = boto3.client('s3')
    client.put_object(Body=more_binary_data, Bucket=BUCKET_NAME, Key=KEY)
    return "new random file: " + KEY

if __name__ == '__main__':
    random_data()