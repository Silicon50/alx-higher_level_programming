#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa
Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Your code should not be executed when imported
"""
import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor and execute the SQL query
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows and print the results
    for state in cur.fetchall():
        print(state)

    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the function to list states
    list_states(username, password, database)
