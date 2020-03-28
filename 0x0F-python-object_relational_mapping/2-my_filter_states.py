#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv

    db = MySQLdb.connect(host="localhost\
", user=av[1], passwd=av[2], db=av[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY \
states.id ASC".format(av[4]))
    for row in cur.fetchall():
        print(row)

    """ cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        # print(row[1], av[4])
        if (row[1] == av[4]):
            print(row) """

    db.close()
    cur.close()
