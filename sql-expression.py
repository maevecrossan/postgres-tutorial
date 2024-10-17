from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from out localhost "chinook" database
# link python file to chinook database
db = create_engine("postgresql:///chinook") #/// shows database is being hosted locally within our workspace environment.

# Will contain a collection of our table objects & data within those objects.
meta = MetaData(db)

#schema:
# create variable for "Artist" table
artist_table = Table(
    "Artist", meta, 
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False), #not foreign key for the sake of this tutorial.
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# connect to database. This saves our connection to the database into a variable called 'connection'.
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
        # if we want to grab results from a single column, we need to wrap the column selection inside of a list.
        # ".c" will identify a specific column header on the table.
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
        # use the .where() method, and from the Name column, looking for only "Queen".
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    #Query 6 - select all tracks from the composer 'Queen' from the "Track" table.
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)