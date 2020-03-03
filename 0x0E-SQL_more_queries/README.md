# SQL - More queries
## Second project about of SQL
MySQL is an open-source database management software that helps users store, organize, and later retrieve data. It has a variety of options to grant specific users nuanced permissions within the tables and databases—this tutorial will give a short overview of a few of the many options.
## Learning Objectives:
 - How to create a new MySQL user
 - How to manage privileges for a user to a database or table
 - What’s a PRIMARY KEY
 - What’s a FOREIGN KEY
 - How to use NOT NULL and UNIQUE constraints
 - How to retrieve datas from multiple tables in one request
 - What are subqueries
 - What are JOIN and UNION
## Requirements:
 - All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
 - All your files should end with a new line
 - All your SQL queries should have a comment just before (i.e. syntax above)
 - All your files should start by a comment describing the task
 - All SQL keywords should be in uppercase (SELECT, WHERE…)
 - A README.md file, at the root of the folder of the project, is mandatory
 - The length of your files will be tested using wc
## Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
## How to import a SQL dump:
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
## Authors:
[Jonatan Mazo](https://www.linkedin.com/in/jonatan-ricardo-mazo-castro-75633390/)
