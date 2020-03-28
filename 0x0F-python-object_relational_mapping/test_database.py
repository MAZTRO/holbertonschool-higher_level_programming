#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv

    db = MySQLdb.connect(host="localhost\
", user='root', passwd='1993', db=av[1], port=3306)
    cur = db.cursor()

    cur.execute("SHOW FULL TABLES FROM {}".format(av[1]))

    for row in cur.fetchall():
        print("({}, '{}')".format(row[0], row[1]))

    db.close()
    cur.close()
