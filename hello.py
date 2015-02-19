from flask import Flask
from flask import render_template
from flask import Response
from flask import request
from random import randint
import json
import boto.ec2
import os

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET']

app = Flask(__name__)

def computation(input):
    num = randint(1, 100)
    return num

def launch_ec2():
    # try except block
    # dictionary.get
    try:
        conn = boto.ec2.connect_to_region("us-east-1", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        conn.run_instances('ami-b0682cd8')#, key_name='myKey', instance_type='t2.micro', security_groups=['sg-c6bc8aa3'])
    except Exception, e:
        print str(e)


def terminate_ec2(instance_id):
    conn = boto.ec2.connect_to_region("us-east", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    conn.terminate_instances(instance_ids=[instance_id])


@app.route('/compute/<int:input>',  methods=['GET'])
def hello_world(input=""):
    data = {}
    if input and request.method == 'GET':
        data['results'] = input * 2
        data['status'] = 200
    else:
        data['status'] = 400


    return Response(json.dumps(data), mimetype='application/json')

if __name__ == '__main__':
    app.run()