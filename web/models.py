def database():
    import mysql.connector
    #Start connection with mysql 
    mydb=mysql.connector.connect(user="root",password='',host='localhost', database='blogwebsite')
    return mydb