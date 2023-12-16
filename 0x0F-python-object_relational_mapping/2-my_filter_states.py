#!/usr/bin/python3
"""
 a script that lists all states with
 a name starting with N (upper N)
 from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    db_name = sys.argv[3]
    input_name = sys.argv[4]

    """
    Access the database and get the states
    """

    my_db = MySQLdb.connect(
            host="localhost", port=3306, user=user_name, passwd=pass_word, db=db_name)

    cs = my_db.cursor()

    cs.execute("SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY states.id ASC".format(input_name))

    rows = cs.fetchall()

    for row in rows:
        print(row)
