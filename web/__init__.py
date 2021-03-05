from flask import Flask,render_template
from web.config import Config 

from jinja2 import Environment,FileSystemLoader


app= Flask(__name__)

from web import views