#!/usr/bin/python3
import MySQLdb
import sys



MY_USER = sys.argv[1]
MY_PASSWORD = sys.argv[2]
MY_DB = sys.argv[3]
MY_HOST = 'localhost'
STATE_NAME_SEARCHED = sys.argv[4]

try:
    # Connect to MySQL server
    dbase = MySQLdb.connect(host='localhost', port=3306, user=MY_USER, passwd='', db=MY_DB)

    # create an instance of exec querys
    cursor = dbase.cursor()

    # Execute the SELECT query and protect to sql injection
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (STATE_NAME_SEARCHED,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))

finally:
    # Close the database connection
    if dbase:
        cursor.close()
        dbase.close()
