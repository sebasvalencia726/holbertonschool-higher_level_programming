#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa where name matches the argument.
The script take 3 arguments: mysql username, mysql password and
database name and state name searched.
The script connects to MySQL server running on localhost at port 3306.
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
The code should not be executed when imported.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states\
               WHERE BINARY name = '{}'\
               ORDER BY id ASC".format(sys.argv[4]))
    tables = c.fetchall()
    for items in tables:
        print(items)
    c.close()
    db.close()
