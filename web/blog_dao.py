
def fetchBlogData(mydb,val):
    sql=f"Select b.b_id,b.bAuthor,b.bTitle,bBlog,b.bLink,b.bDate ,c.cName \
        from blogdata as b \
        INNER JOIN category c \
        ON b.bCategory = c.c_id \
        where b.b_id = {val};"
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    # print("_________________________________________________________")
    # print(data)
    # print("yoyo_________________________________________________________")
    return data

def insert_new_blog(mydb,data):
    cursor=mydb.cursor()
    sql="INSERT INTO blogdata ( bTitle,bAuthor,bBlog,bCategory,bLink,bDate,bEdit) VALUES (%s, %s, %s, %s, %s ,%s,' ');"
    cursor.execute(sql, data)
    mydb.commit()
    return cursor.lastrowid

def updateBlogData(mydb,val):
    cur=mydb.cursor()
    sql="UPDATE blogdata SET bTitle = %s, bAuthor = %s,bEdit = 'Edited', bLink = %s, bBlog = %s WHERE (b_id = %s);"
    cur.execute(sql, val)
    mydb.commit()

def deleteBlog(connection,val):
    cursor=connection.cursor()
    query='DELETE FROM blogdata where b_id=' + str(val)
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid
    
def showFilterAllBlogs(mydb,col,ord,val):

    mycursor=mydb.cursor()
    val=str(val)
    sql=f'Select b.b_id,b.bAuthor,b.bTitle,bBlog,b.bLink,b.bDate ,c.cName \
        from blogdata as b \
        INNER JOIN category c \
        ON b.bCategory = c.c_id \
            where b.b_id !={val} \
         order by {col} {ord}'

    mycursor.execute(sql)
    myresult=mycursor.fetchall() 
    #print(myresult) 
    return myresult


def fetchUsersData(mydb,val):
    val=str(val)
    sql=f"Select b.b_id,b.bAuthor,b.bTitle,bBlog,b.bLink,b.bDate ,c.cName \
        from blogdata as b \
        INNER JOIN category c \
        ON b.bCategory = c.c_id \
            Where bAuthor='{val}' and b_id not in (select p_id from published)\
         order by bDate ASC ;\
         "
    # print(sql)
    print('fetching data from database to get author\'s all blogs ...')
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    # print("_________________________________________________________")
    # print(data)
    # print("yoyo_________________________________________________________")
    return data

def executeSql(mydb):
    sql='ALTER TABLE `blogwebsite`.`published` \
            ADD CONSTRAINT `fp_id`\
            FOREIGN KEY (`p_id`)\
            REFERENCES `blogwebsite`.`blogdata` (`b_id`)\
            ON DELETE NO ACTION\
            ON UPDATE RESTRICT;'

    cur=mydb.cursor()
    cur.execute(sql)
    mydb.commit

def showAllBlogs(mydb):
    mycursor=mydb.cursor()
    sql='Select b.b_id,b.bAuthor,b.bTitle,bBlog,b.bLink,b.bDate ,c.cName \
        from blogdata as b \
        INNER JOIN category c \
        ON b.bCategory = c.c_id \
         order by b.bDate DESC'
    mycursor.execute(sql)
    myresult=mycursor.fetchall() 
    #print(myresult) 
    return myresult

def getCategories(mydb):
    sql="SELECT c_id,cName FROM blogwebsite.category\
         where c_id != '1' order by cName;"
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    return data

def getPublishedBlogList(mydb):
    sql='SELECT p_id,b.bAuthor,b.bTitle,bBlog,b.bLink,p_date,c.cName,p_likes \
            FROM blogwebsite.published as p \
            Inner join blogdata as b \
            On p.p_id=b.b_id \
            Inner join category as c \
            On b.bCategory = c.c_id;'

    
    a=["p_id","b.bAuthor","b.bTitle","bBlog","b.bLink","p_date","p_likes"]
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    # print(data)
    return data



def getPublishedBlogListOfUser(mydb,user=None):
    sql=f'SELECT p_id,b.bAuthor,b.bTitle,bBlog,b.bLink,p_date,c.cName,p_likes \
            FROM blogwebsite.published as p \
            Inner join blogdata as b \
            On p.p_id=b.b_id \
            Inner join category as c \
            On b.bCategory = c.c_id \
            where b.bAuthor="{user}";'

    a=["p_id","b.bAuthor","b.bTitle","bBlog","b.bLink","p_date","p_likes"]
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    return data
from datetime import date

def addIdToPublishTable(mydb,val):
    
    sql='Insert Into published Values (%s,%s,"0");'
    v=(val,date.today())
    print('000000',date.today())
    print(v)
    cur=mydb.cursor()
    cur.execute(sql,v)
    mydb.commit()