import os
from flask import Flask,request,make_response,jsonify
import requests

api_url = os.getenv('API_URL')
app = Flask(__name__)


def headers():
    return dict(request.headers)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['get'])
def get_all(u_path):
    url = api_url+u_path
    print(url)
    return requests.get(url=url,data=None,json=None,headers=headers()).content


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['post'])
def post_all(u_path):
    print(repr(u_path))
    return "welcomme home post"

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['put'])
def put_all(u_path):
    print(repr(u_path))
    return "welcomme home put"

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['patch'])
def patch_all(u_path):
    print(repr(u_path))
    return "welcomme home patch"

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['delete'])
def delete_all(u_path):
    print(repr(u_path))
    return "welcomme delete"

if __name__=='__main__':
    app.run(debug=True)