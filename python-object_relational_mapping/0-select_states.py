#!/usr/bin/python3
import MySQLdb
import sys


if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

MY_USER = sys.argv[1]
MY_PASSWORD = sys.argv[2]
MY_DB = sys.argv[3]
MY_HOST = 'localhost'

try:
    # Connect to MySQL server
    db = MySQLdb.connect(host=MY_HOST, port=3306, user=MY_USER,
                         passwd='', db=MY_DB)

    # create an instance of exec querys
    cursor = db.cursor()

    # Execute the SELECT query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))

finally:
    # Close the database connection
    if db:
        cursor.close()
        db.close()
