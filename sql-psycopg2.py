import  psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database (like a set,list/array)
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table.
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from "Artist" table. (Placeholder due to quotes)
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table.
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', ["51"])

# Query 5 - select only by "ArtistId" #51 from the "Artist" table.
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["51"])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table.
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - select all tracks where the composer is not in the table.
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Taylor Swift"])

# Query 8 - select all tracks where the composer is "AC/DC" from the "Track" table.
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# fetch the results (multiple) from the cursor
results = cursor.fetchall()

# fetch the results (single) from the cursor
# results = cursor.fetchone()

# close connection 
connection.close()

# print results
for result in results:
    print(result)