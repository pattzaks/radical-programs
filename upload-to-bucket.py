# This program creates a bucket and uploads a file in it
# @Author : Akshay Patil


import json
import requests as r
import boto
import uuid
from boto.s3.connection import S3Connection


conn = S3Connection (access_key_id, secret_access_key)

bucket_name = "bucket-bikram"
print "Creating new Bucket with %s"%bucket_name
bucket = conn.create_bucket(bucket_name)

''' -   - - - -- - - - - -- - - - - - - -- - - -- -- - - -  - - - '''

from boto.s3.key import Key
k = Key(bucket)
k.key  = "file1"
print "Uploading some data to " + bucket_name + " with key :" + k.key

#TODO : change this to the file you want to upload
k.set_contents_from_filename("/home/akshay/Desktop/sample-radical-12")
