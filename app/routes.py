from app import app
from flask import render_template
@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'admin'}
    posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    },
    {
        'author': {'username': 'Devansh'},
        'body': 'Exploring the depths of Python is always exciting!'
    },
    {
        'author': {'username': 'Alice'},
        'body': 'Just finished reading a fantastic book on AI!'
    },
    {
        'author': {'username': 'Bob'},
        'body': 'Had the best coffee today at a small local shop.'
    },
    {
        'author': {'username': 'Michael'},
        'body': 'Climbed a mountain this weekend, what a view!'
    },
    {
        'author': {'username': 'Jessica'},
        'body': 'Started learning web development. So far, so good!'
    },
    {
        'author': {'username': 'David'},
        'body': 'I can’t believe how fast this year is flying by.'
    },
    {
        'author': {'username': 'Emily'},
        'body': 'Loving the fall season, the colors are amazing!'
    },
    {
        'author': {'username': 'Chris'},
        'body': 'Just launched my new blog on tech trends!'
    }
]
    return render_template('index.html', title='Home', user=user, posts=posts)