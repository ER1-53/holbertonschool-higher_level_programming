#!/usr/bin/python3
import MySQLdb
import sys


if len(sys.argv) != 5:
    print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
    sys.exit(1)

MY_USER = sys.argv[1]
MY_PASSWORD = sys.argv[2]
MY_DB = sys.argv[3]
MY_HOST = 'localhost'
States = sys.argv[4]


try:
    # Connect to MySQL server
    db = MySQLdb.connect(host=MY_HOST, port=3306, user=MY_USER, passwd='', db=MY_DB)

    # create an instance of exec querys
    cursor = db.cursor()

    # Execute the SELECT query and protect to sql injection
    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id", (States,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    """test = 0
    for row in rows:
        if test < 1:
            print(", ".join(row),end="")
            test = 1 
        else:
            print(", ", end="")
            print(", ".join(row),end="") 
    print()"""
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    
except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))

finally:
    # Close the database connection
    if db:
        cursor.close()
        db.close()
