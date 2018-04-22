import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='')
print(connection.get_server_version())
connection.close()
