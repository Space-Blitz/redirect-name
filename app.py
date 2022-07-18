import os
from flask import Flask,request,jsonify
from flask_cors import CORS
import requests

api_url = os.getenv('API_URL')
app = Flask(__name__)
CORS(app)

def headers():
    return {'Authorization':request.headers.get('Authorization')}


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['get'])
def get_all(u_path):
    response=''
    try:
        url = api_url+u_path
        response = requests.get(url=url,headers=headers())
        return jsonify(response.json()),response.status_code
    except:
        return jsonify(response.json()),response.status_code


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['post'])
def post_all(u_path):
    response=''
    try:
        url = api_url+u_path
        response = requests.post(url=url,headers=headers(),json=request.get_json(force=True))
        return jsonify(response.json()),response.status_code
    except:
        return jsonify(response.json()),response.status_code

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['put'])
def put_all(u_path):
    response=''
    try:
        url = api_url+u_path
        response = requests.put(url=url,headers=headers(),json=request.get_json(force=True))
        return jsonify(response.json()),response.status_code
    except:
        return jsonify(response.json()),response.status_code


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['patch'])
def patch_all(u_path):
    response=''
    try:
        url = api_url+u_path
        response = requests.patch(url=url,headers=headers(),json=request.get_json(force=True))
        return jsonify(response.json()),response.status_code
    except:
        return jsonify(response.json()),response.status_code

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>',methods=['delete'])
def delete_all(u_path):
    response=''
    try:
        url = api_url+u_path
        response = requests.delete(url=url,headers=headers())
        return jsonify(response.json()),response.status_code
    except:
        return jsonify(response.json()),response.status_code

if __name__=='__main__':
    app.run(debug=True)