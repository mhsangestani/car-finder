# import the sqlite3 library
import sqlite3

# create a connection to the database
conn = sqlite3.connect('Car.db')

# create a cursor object to interact with the database
c = conn.cursor()

# create a table called 'Information' if it does not already exist
c.execute('''CREATE TABLE IF NOT EXISTS Information (
            name text,
            miles text,
            price text
                        ) ''')

# define a function to insert car information into the database
def insert_car(list_Information):
    # use a context manager to ensure all changes are committed to the database
    with conn:
        # execute an SQL statement to insert data into the 'Information' table
        c.execute('INSERT INTO Information VALUES (?,?,?)',(list_Information[0],list_Information[1],list_Information[2]))

# define a function to retrieve all car information from the database
def get_car():
    # execute an SQL statement to select all rows from the 'Information' table
    c.execute('SELECT * FROM Information')
    # return all results as a list of tuples
    return c.fetchall()
