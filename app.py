import os
from flask import Flask,request,make_response,jsonify
import requests

api_url = os.getenv('API_URL')
app = Flask(__name__)


def headers():
    return {'Authorization':request.headers.get('Authorization')}
    # return dict(request.headers)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['get'])
def get_all(u_path):
    url = api_url+u_path
    return requests.get(url=url,headers=headers()).content


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['post'])
def post_all(u_path):
    url = api_url+u_path
    return requests.post(url=url,headers=headers(),json=request.get_json(force=True)).content

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['put'])
def put_all(u_path):
    url = api_url+u_path
    return requests.post(url=url,headers=headers(),json=request.get_json(force=True)).content

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['patch'])
def patch_all(u_path):
    url = api_url+u_path
    return requests.patch(url=url,headers=headers(),json=request.get_json(force=True)).content

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['delete'])
def delete_all(u_path):
    url = api_url+u_path
    return requests.delete(url=url,headers=headers()).content

if __name__=='__main__':
    app.run(debug=True)