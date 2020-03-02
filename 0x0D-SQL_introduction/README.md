# SQL - Introduction
## Project 0x0D SQL
MySQL is an open source database management software that helps users store, organize, and retrieve data. It is a very powerful program with a lot of flexibility—this tutorial will provide the simplest introduction to MySQL.
## How to Install MySQL on Ubuntu:
If you don't have MySQL installed on your droplet, you can quickly download it.
```sudo apt-get install mysql-server```
## How to Access the MySQL shell
Once you have MySQL installed on your droplet, you can access the MySQL shell by typing the following command into terminal:
```mysql -u root -p``` o  ```mysql -hlocalhost -uroot -p```
## Learning Objectives:
 - What’s a database
 - What’s a relational database
 - What does SQL stand for
 - What’s MySQL
 - How to create a database in MySQL
 - What does DDL and DML stand for
 - How to CREATE or ALTER a table
 - How to SELECT data from a table
 - How to INSERT, UPDATE or DELETE data
 - What are subqueries
 - How to use MySQL functions
## Requirements:
 - All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
 - All your files should end with a new line
 - All your SQL queries should have a comment just before (i.e. syntax above)
 - All your files should start by a comment describing the task
 - All SQL keywords should be in uppercase (SELECT, WHERE…)
 - A README.md file, at the root of the folder of the project, is mandatory
 - The length of your files will be tested using wc
## More Info:
### Comments for your SQL file:
```
$
$
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
$
$
```
## Authors:
[Jonatan Mazo](https://www.linkedin.com/in/jonatan-ricardo-mazo-castro-75633390/)
