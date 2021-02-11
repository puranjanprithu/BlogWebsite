from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from web.config import Config 

app= Flask(__name__) #made instance of our app

#db= SQLAlchemy(app)
# from web import models 
from web import views
#from web.Admin.views import admin
#app.register_blueprint(admin,url_prefix="/admin")


