#!/usr/bin/python3
"""
    a script that lists all states with a name starting
    with 'N'
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    for state in cur.fetchall():
        if state[1][0] == "N":
            print(state)
