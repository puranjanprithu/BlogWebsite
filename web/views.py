from flask import  Flask,render_template
from web import app

@app.route('/',methods=['GET'])
def index():
   return render_template("index.html")

@app.route('/home')
def home():
   return render_template("home.html")

@app.route('/home/<string:name>/<int:id>')
def dynamicRoute(name,id):
   
   return "Hello user: " + name +" your id is " + str(id)

@app.route('/topics')
def topics():
   return render_template("topics.html")

@app.route('/info')
def info():
   return render_template("info.html")