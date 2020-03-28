#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv

    db = MySQLdb.connect(host="localhost\
", user=av[1], passwd=av[2], db=av[3], port=3306)

    cur = db.cursor()

    if (len(av) > 4):
        if ("TRUNCATE" in av[4]):
            state = av[4].split(';')
            st = state[0].split("'")
            sts = st[0]
        else:
            sts = av[4]

    cur.execute("SELECT cities.name FROM cities, states WHERE \
states.name = %s AND cities.state_id = states.id ORDER BY \
cities.id ASC", (sts,))

    data = cur.fetchall()
    for idx in range(len(data)):
        if (idx < len(data) - 1):
            print(data[idx][0], end=", ")
        else:
            print(data[idx][0])

    db.close()
    cur.close()
