# Object-relational mapping
## Project 0x0F in Python
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

## Learning Objectives:
 - Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
 - How to connect to a MySQL database from a Python script
 - How to SELECT rows in a MySQL table from a Python script
 - How to INSERT rows in a MySQL table from a Python script
 - What ORM means
 - How to map a Python Class to a MySQL table
## Requirements:
 - Your files will be executed with MySQLdb version 1.3.x
 - Your files will be executed with SQLAlchemy version 1.2.x
 - All your files should end with a new line
 - The first line of all your files should be exactly #!/usr/bin/python3
 - A README.md file, at the root of the folder of the project, is mandatory
 - Your code should use the PEP 8 style (version 1.7.*)
 - All your files must be executable
 - The length of your files will be tested using wc
 - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
 - You are not allowed to use execute with sqlalchemy
## More info:
For installing MySQLdb, you need to have MySQL installed:
```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
```
==============================================
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__
'1.3.10'
```
Install SQLAlchemy module version 1.2.x:
```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.2.5'
```
## Authors:
[JonataM](https://www.linkedin.com/in/jonatan-ricardo-mazo-castro-75633390/)
