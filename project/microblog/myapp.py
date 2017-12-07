#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' my flask app '''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is my first flask app'
@app.route('/hello')
def hello():
    return 'hello world'
@app.route('/projects/')
def projects():
    return 'the projects page'
@app.route('/about')
def about():
    return 'the about page'
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User is {}'.format(username)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)
