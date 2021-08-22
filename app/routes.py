from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    heading = 'Sly couch Survivor'
    desc = "stuff stuff and more stuff"
    key_points = ['Point 1', 'Point 2', 'Point 3']
    html_points = '<ul>'
    for item in key_points:
        html_points += f'<li>{item}</li>'
    html_points += '</ul>'
    return f'<h1> {heading}</h1><p>{desc}</p>{html_points}'