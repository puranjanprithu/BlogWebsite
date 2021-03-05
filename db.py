from datetime import datetime

#Start connection with mysql 
import mysql.connector
mydb=mysql.connector.connect(user="root",password='',host='localhost', database='blogwebsite')
mycursor=mydb.cursor()

sql="Select * from blogdata"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)
print()
print(myresult)