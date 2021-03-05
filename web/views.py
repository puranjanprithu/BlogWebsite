from flask import  Flask,render_template,request,redirect
from web import app
from web.models import database
# @app.route('/',methods=['GET'])
# def index():
#    return render_template("index.html")

# @app.route('/home')
# def home():
#    return render_template("home.html")

mydb=database()

@app.route('/blog/<int:blogid>')
def posts(blogid):
    colname=['Author','Date and Time','Category','Link','Content']
    val=int(blogid)
    sql=f"Select b.b_id,b.bAuthor,b.bTitle,bBlog,b.bImage,b.bDate ,c.catValue \
        from blogdata as b \
        INNER JOIN category c \
        ON b.bCategory = c.cat_id \
        where b.b_id = {val};"
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    print("_________________________________________________________")
    print(data)
    print("_________________________________________________________")
    return render_template("posts.html",blog=data)

@app.route('/info')
def info():
   return render_template("info.html")


@app.route('/')
def index():
    
    #sql to get all values from table blogdata
    mycursor=mydb.cursor()
    sql="Select b.b_id,b.bAuthor,b.bTitle,bBlog,b.bImage,b.bDate ,c.catValue \
        from blogdata as b \
        INNER JOIN category c \
        ON b.bCategory = c.cat_id \
         order by b.bDate DESC"
    mycursor.execute(sql)
    myresult=mycursor.fetchall() 
    #print(myresult) 
    return render_template('index.html',albums=myresult, title="Database blog")

@app.route('/forms',methods=['GET','POST'])
def forms():
    print(request.method,request,request.args,"........................................................................................................................")
    #handle get request
    if request.method=='GET':
        if 'name' in request.args:
            nam=request.args['name']
            print(nam)

    if request.method=='POST':
        
            age=request.form['age']
            print(age)

    return render_template('forms.html')

@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        bt=request.form['bTitle']
        ba=request.form['bAuthor']
        btxt=request.form['bText']
        bc=request.form['bCategory']
        bi=request.form['bImage']
        l=[bt,ba,btxt,bc,bi]
        print(l)
        cur=mydb.cursor()
        sql = "INSERT INTO blogdata ( bTitle,bAuthor,bBlog,bCategory,bImage) VALUES (%s, %s, %s, %s, %s)"
        val = (bt,ba,btxt,bc,bi)
        cur.execute(sql, val)
        mydb.commit()
    return render_template("home.html")