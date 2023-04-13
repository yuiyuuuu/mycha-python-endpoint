import json
import sys
import boto3
import pickle

from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), '../../.env')
values = load_dotenv(dotenv_path)


def upload_file(filename, data):
    #open up access to s3
    s3 = boto3.client('s3', 
                      region_name='us-east-2',
                      aws_access_key_id=os.environ.get("ACCESS_KEY"),
                      aws_secret_access_key=os.environ.get("SECRET_KEY"))
    
    pickle.dump( data, open( filename, "wb" ) )
    s3.upload_file(filename, 'mycha-inventory', filename)
    
location_stock = json.loads(sys.argv[1])
location_name = json.loads(sys.argv[2])


upload_file(location_name+"_stock-data", location_stock)
print("success")


