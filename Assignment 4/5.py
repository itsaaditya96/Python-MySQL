import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """SELECT quotationid, quotationdate,quotedprice 
            FROM quotation WHERE 
            quotedprice BETWEEN 1400 and 2150;"""
cur.execute(sql)
data = cur.fetchall();
for row in data:
    print(row)
connection.commit()
connection.close()
