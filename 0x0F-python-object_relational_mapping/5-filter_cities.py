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

    cur.execute("""SELECT cities.name FROM states, cities \
WHERE states.id = cities.state_id AND states.name = %s \
ORDER BY cities.id ASC""", (sts,))

    data = cur.fetchall()

    rows = list(map(''.join, data))
    print(', '.join(rows))

    cur.close()
    db.close()
