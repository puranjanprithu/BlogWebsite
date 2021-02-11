from flask import Blueprint,request,render_template
from web import app
from web.models import Admin



admin=Blueprint("Admin",__name__)

@admin.route("/",methods=['GET','POST'])
def log_in():
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["passcode"]

        user=Admin.query.filter_by(email=email).first()
        if user.password==pwd:
            flash("You are logged in ",success)
        flash("You are not an admin!!","danger")
        return redirect(url_for('Admin.log_in'))



    return render_template()