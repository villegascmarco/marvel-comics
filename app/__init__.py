from urllib import response
from flask import Flask, make_response, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    return f"Hello World aa flask from {request.cookies.get('user_ip')}"
