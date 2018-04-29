import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
cur.executemany("""UPDATE item SET 
                price = price*%s where itemtype=%s;""",
                [('1.03','FMCG'),
                 ('1.05','Apparels'),
                 ('1.11','Computer')])
connection.commit()
connection.close()
