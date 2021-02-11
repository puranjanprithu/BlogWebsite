#object relational mapper - 
# con= sqlite3.connect("test.db")
# cursor=con.cursor()
# cursor.execute("")

from web import db
from datetime import datetime
class Admin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(120),nullable=False)

    def __repr__(self):
        return "Admin('Email','Password')"
class Blogs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text, nullable=False,unique=True)
    img=db.Column(db.String(120),nullable=False)
    date_posted=db.Column(db.DateTime,nullabl=False, default=datetime.now())













