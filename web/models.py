def database():
    import mysql.connector
    #Start connection with mysql 
    mydb=mysql.connector.connect(user="root",password='root',host='127.0.0.1', database='blogwebsite')
    return mydb
    # jn6s8pzkBLkhKnx