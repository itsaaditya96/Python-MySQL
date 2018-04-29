import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
cur.executemany("""INSERT INTO supplier VALUES(%s,%s,%s,%s)""",
                [('S1006','Frank Stores','123-345-456','frankstores@gmail.com'),
                ('S1007','Anshika Stores','456-345-456','anshikastores@gmail.com')])
connection.commit()
connection.close()
