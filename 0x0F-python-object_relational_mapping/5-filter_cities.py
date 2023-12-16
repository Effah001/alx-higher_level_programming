#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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
            host="localhost", port=3306, user=user_name,
            passwd=pass_word, db=db_name)

    cs = my_db.cursor()

    query = (
            "SELECT c.name "
            "FROM cities c INNER JOIN states s "
            "ON c.state_id = s.id "
            "WHERE s.name LIKE %s "
            "ORDER BY c.id "
       )
    
    cs.execute(query, (input_name + '%', ))
    
    rows = cs.fetchall()
    output = ", ".join(row[0] for row in rows)
    print(output)
