from flask import Flask #, request, redirect
import random
import cgi
import os
import jinja2 

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
   loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

app = Flask(__name__)


@app.route('/')
def hello():

    template = jinja_env.get_template('signup_form.html')
    return template.render()

app.run