import mysql.connector

conn = mysql.connector.connect(user='myprotek',password='mypassword',host='myprotek.cisaw8k67dxp.us-east-1.rds.amazonaws.com',database='myprotek')
mycursor = conn.cursor()
# mycursor.execute("update mytable set id=3 where name='rakesh'")
# conn.commit()
mycursor.execute('SELECT * FROM mytable')

print mycursor.fetchall()