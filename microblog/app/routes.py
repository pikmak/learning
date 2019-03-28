# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'pussein'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool!'
        },
        {
            'author': {'username': 'Lohpidr'},
            'body': 'Sam lohpidr'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
