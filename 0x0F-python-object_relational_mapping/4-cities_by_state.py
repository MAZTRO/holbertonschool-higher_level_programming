#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv

    db = MySQLdb.connect(host="localhost\
", user=av[1], passwd=av[2], db=av[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC")

    for row in cur.fetchall():
        print(row)

    db.close()
    cur.close()
