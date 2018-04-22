# Python-MySQL
Performing Database operations on MySQL using Python

## Assignment 1

Objective: Learn how to connect to MySQL Server and execute SQL Commands using python programming

Problem Description: Easy Shop retial application need a database application to maintain their customer and purchase details. Write a python program to establish a database connectivity between MySQL and python.

### Step 1

To Start, we need to install the driver mysql-python connector, download it from link below: -
https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.11.zip

After Downloading, Extract the zip

Enter the following command to windows command line
```
cd <extracter zip path>\
python setup.py install
```

Note = You'll need to add python to *System Variables under *Environmental Variables to execute installation command

### Step 2
#### Use below command to import MySQL Connector
```
import mysql.connector;
```

### Step 3
#### Creating cursor for executing commands
```
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='')   '''Connection String'''
cur = cur = connection.cursor();
```

### Step 4
#### Connecting to Database and Execution Command
```
cur.execute("Select * from supplier;")
data = cur.fetchall();
```

### Step 5
#### Committing data into Database
```
connection.commit()
```
For rollback use: -
```
connection.rollback()
```

Summary of this assignment: To learn database connection of python with MySQL Server.

## Assignment 2


