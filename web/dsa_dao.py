def getDSList(mydb):
    sql="SELECT d_id,ds_name, ds_easy, ds_medium, ds_hard FROM data_structure;"
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    return data

def insertDSRow(mydb,val):
    # sql="INSERT INTO data_structure (ds_name, ds_easy, ds_medium, ds_hard) VALUES (%s,0,0,0);"
    sql=f"INSERT INTO `blogwebsite`.`data_structure` (`ds_name`, `ds_easy`, `ds_medium`, `ds_hard`) VALUES ('{val}', '0', '0', '0');"
    print(sql )
    cursor=mydb.cursor()
    try:
        cursor.execute(sql)
        mydb.commit()
    except:
        print("duplicate entry")
    return cursor.lastrowid

def updateDSRow(mydb,val):
    
    sql="UPDATE data_structure SET ds_easy = %s, ds_medium = %s, ds_hard = %s WHERE (d_id = %s);"
    cur=mydb.cursor()
    cur.execute(sql, val)
    mydb.commit()


