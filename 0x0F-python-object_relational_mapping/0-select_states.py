#!/usr/bin/python3

import MySQLdb
import sys


    user_name = sys.argv[1]
    pass_word sys.argv[2]
    db_name = sys.argv[3]

    connection = MySQLdb.connect(host="localhost", port=3306, user=user_name, passwd=pass_word, db=db_name)

    cs = connection.cursor()

    cs.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cs.fetchall()

    for row in rows:
        print(row)

    if __name__ == "__main__":
