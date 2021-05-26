from flask import  Flask,render_template,request,redirect
from web import app
import webbrowser
from web.models import database
from web.blog_dao import getPublishedBlogListOfUser,addIdToPublishTable,deleteBlog,fetchBlogData,getCategories,updateBlogData,showAllBlogs,insert_new_blog,showFilterAllBlogs,fetchUsersData,getPublishedBlogList
from web.dsa_dao import getDSList,insertDSRow,updateDSRow
from datetime import datetime
# @app.route('/',methods=['GET'])
# def index():
#    return render_template("index.html")

# @app.route('/home')
# def home():
#    return render_template("home.html")



mydb=database()
@app.route('/',methods=['GET','POST'])
def index():
    myresult=showAllBlogs(mydb)
    publishedData=getPublishedBlogList(mydb)
    return render_template('index.html',albums=myresult, title="Database blog")

@app.route('/blog/<int:blogid>',methods=['GET','POST'])
def posts(blogid):
    colname=['Author','Date and Time','Category','Link','Content']
    val=int(blogid)
    

    if request.method=='POST':
        bt=request.form['title']
        ba=request.form['author']
        #bc=request.form['category']
        bl=request.form['link']
        btxt=request.form['content']
        
                
        v = (bt,ba,bl,btxt,val)
        updateBlogData(mydb,v)

        btn=request.form['action']
        if btn=='Update':
           print("updated")
        elif btn=='Delete':
            deleteBlog(mydb,val)
            webbrowser.open(f"/blog/{val+1}", new=0)
        elif btn=='Publish':
            addIdToPublishTable(mydb,val)

    return render_template("blog.html",blog=fetchBlogData(mydb,val),val=val)
        
    

    
    
    

@app.route('/info')
def info():
   return render_template("info.html")






@app.route('/home',methods=['GET','POST'])
def home():
    user='patrik rothfus'
    if request.method=='POST':
        bt=request.form['bTitle']
        ba=request.form['bAuthor']
        btxt=request.form['bText']
        bc=request.form['bCategory']
        bi=request.form['bImage']
        # l=[bt,ba,btxt,bc,bi]
        # print(l)
        if bc=='...':
            bc=1
        data = (bt,ba,btxt,bc,bi,datetime.now())
        insert_new_blog(mydb,data)
    return render_template("home.html",userBlogs=fetchUsersData(mydb,user),categoriesList=getCategories(mydb), 
                            pubBlogs=getPublishedBlogListOfUser(mydb,user))

@app.route('/page/<int:blogid>',methods=['GET','POST'])
def page(blogid):
    val=int(blogid)
    col=['b_id','bTitle','bDate','bAuthor']
    ord1=['ASC','DESC']
    i=0
    j=0
    b=fetchBlogData(mydb,val)
    
    #right column sorting
    if 'Category' in request.args:
            bc=int(request.args["Category"])
            j=int(request.args["Order"])
            
    print(i,'enter the dragon')

    return render_template("userpage.html",blog=b,rightList=showFilterAllBlogs(mydb,col[i],ord1[j],val),val=val)

@app.route('/forms',methods=['GET','POST'])
def forms():
    print(request.method,request,request.args,"........................................................................................................................")
    #handle get request
    if request.method=='GET':
        if 'name' in request.args:
            nam=request.args['name']
            # nam=request.form['name']
            print(nam)

    if request.method=='POST':
            
            

            bt=request.form['action']
            
            if bt=='Insert':
                dname=request.form['dsa_name']
                dname=dname.lower()
                insertDSRow(mydb,dname)
                print('Inserted data',str(dname))

            elif bt=='Update':
                dsId=request.form['ds_id']
                deasy=request.form['ds_easy']
                dmedium=request.form['ds_medium']
                dhard=request.form['ds_hard']
                val=(deasy,dmedium,dhard,dsId)
                updateDSRow(mydb,val)
                print(val)

            print(bt)


    return render_template('forms.html',dsList=getDSList(mydb))