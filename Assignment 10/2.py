import mysql.connector

connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
cur.execute("""SELECT s.supplierid,suppliername,itemcode,quotedprice,COUNT(s.supplierid) 
            FROM supplier s,quotation q WHERE s.supplierid = q.supplierid 
            and quotationstatus = 'Accepted' GROUP BY supplierid""")
for row in cur.fetchall():
    print(row)
connection.close()
