#!/user/bin/python3
# -*-coding:utf-8-*-
# @Author: qsl
# @Date: 2018-07-11 16:11:08
# @Last Modified by:   qsl
# @Last Modified time: 2018-07-11 16:11:08
# @Description: Description

# https://code.visualstudio.com/docs/python/tutorial-flask

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'
