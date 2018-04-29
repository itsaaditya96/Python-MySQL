# Python-MySQL
Performing Database operations on MySQL using Python

## Assignment 1 - Database Connection: : Guided Activity

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

Note: You'll need to add python to *System Variables under *Environmental Variables to execute installation command

### Step 2
#### Use below command to import MySQL Connector
```
import mysql.connector;
```

### Step 3
#### Creating cursor for executing commands
```
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='')   '''Connection String'''
cur = connection.cursor();
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

## Assignment 2 - Database Connection: Hands-On

Create Commands


## Assignment 3 - Database: Retrieve Data : Guided Activity

Objective: Given a real time problem, to search for a particular supplier and display the details

Problem Description: Consider the scenario to display supplier details using different fetch methods.

#### Code 1: Display all records from the table:
```
cur.fecthall()
```

#### Code 2: Display or fetch one record at a time from the database.
```
cur.fecthone()
```

#### Code 3: Display or fetch many records from the database.
```
cur.fecthmany()
```


## Assignment 4 - Database: Retrieve Data: Hands-On

Objective: In continuation to Assignment 2 Hands-On and use SELECT operations to reterive and display records using python code.

Problem Description:
1. Retrieve all the records of item table.
2. Retrieve the supplier name and supplier’s contact number of the supplier ‘S1002’.
3. Retrieve the quotation id and supplier id of the quotations which have been either ‘Accepted’ or ‘Rejected’.
4. Retrieve supplier details like supplier id and supplier name whose names have ‘i’ as the second character
5. Retrieve the quotation details like quotationid, quotationdate, quotedprice for those quotations which are quoted in the range of 1400 and 2150


## Assignment 5 - Database: Passing Parameters : Guided Activity
