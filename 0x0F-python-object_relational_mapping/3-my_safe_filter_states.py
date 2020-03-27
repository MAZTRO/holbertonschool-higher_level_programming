#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv

    db = MySQLdb.connect(host="localhost\
", user=av[1], passwd=av[2], db=av[3], port=3306)

    cur = db.cursor()

    """ if ("TRUNCATE" in av[4]):
        state = av[4].split(';')
        state[0].strip("'")

    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY \
states.id ASC".format(state[0].strip("'")))

    for row in cur.fetchall():
        print(row) """

    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        # print(row[1], av[4])
        if (row[1] == av[4]):
            print(row)
