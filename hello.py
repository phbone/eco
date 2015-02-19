from flask import Flask
from flask import render_template
from flask import Response
from flask import request
from random import randint
import json

app = Flask(__name__)

def computation(input):
    num = randint(1, 100)
    return num


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