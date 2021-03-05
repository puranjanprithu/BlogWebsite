from flask import Flask,render_template
from web.config import Config 

app= Flask(__name__) #made instance of our app

from web import views



