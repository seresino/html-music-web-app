# from lib.album_repository import *
# from lib.album import *

# """
# When we call AlbumRepository#all
# We get a list of Album objects reflecting the seed data.
# """
# def test_all_album(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
#     repository = AlbumRepository(db_connection) # Create a new AlbumRepository

#     albums = repository.all() # Get all albums

#     # Assert on the results
#     assert albums == [
#         Album(1, 'Doolittle', 1989, 1),
#         Album(2, 'Surfer Rosa', 1988, 1),
#         Album(3, 'Waterloo', 1974, 2),
#         Album(4, 'Super Trouper', 1980, 2),
#         Album(5, 'Bossanova', 1990, 1),
#         Album(6, 'Lover', 2019, 3),
#         Album(7, 'Folklore', 2020, 3),
#         Album(8, 'I Put a Spell on You', 1965, 4),
#         Album(9, 'Baltimore', 1978, 4),
#         Album(10, 'Here Comes the Sun', 1971, 4),
#         Album(11, 'Fodder on My Wings', 1982, 4),
#         Album(12, 'Ring Ring', 1973, 2),
#     ]

# """
# When we call AlbumRepository#find with an id
# We get a single Album object corresponding to the id back
# """
# def test_find_album(db_connection):
#     db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
#     repository = AlbumRepository(db_connection) # Create a new AlbumRepository

#     album = repository.find(1)
#     assert album == Album(1, 'Doolittle', 1989, 1)

# """
# When we call AlbumRepository#create with a title, release_year, and artist_id,
# We get a new record in the database
# """
# def test_create_album(db_connection):
#     db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
#     repository = AlbumRepository(db_connection) # Create a new AlbumRepository

#     repository.create(Album(None, 'Arrival', 1976, 2))

#     result = repository.all()
#     assert result == [
#         Album(1, 'Doolittle', 1989, 1),
#         Album(2, 'Surfer Rosa', 1988, 1),
#         Album(3, 'Waterloo', 1974, 2),
#         Album(4, 'Super Trouper', 1980, 2),
#         Album(5, 'Bossanova', 1990, 1),
#         Album(6, 'Lover', 2019, 3),
#         Album(7, 'Folklore', 2020, 3),
#         Album(8, 'I Put a Spell on You', 1965, 4),
#         Album(9, 'Baltimore', 1978, 4),
#         Album(10, 'Here Comes the Sun', 1971, 4),
#         Album(11, 'Fodder on My Wings', 1982, 4),
#         Album(12, 'Ring Ring', 1973, 2),
#         Album(13, 'Arrival', 1976, 2)
#     ]

# """
# When we call AlbumRepository#delete with an id
# We delete the corresponding album from the table
# """
# def test_delete_album(db_connection):
#     db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
#     repository = AlbumRepository(db_connection) # Create a new AlbumRepository

#     repository.delete(2)

#     result = repository.all()
#     assert result == [
#         Album(1, 'Doolittle', 1989, 1),
#         Album(3, 'Waterloo', 1974, 2),
#         Album(4, 'Super Trouper', 1980, 2),
#         Album(5, 'Bossanova', 1990, 1),
#         Album(6, 'Lover', 2019, 3),
#         Album(7, 'Folklore', 2020, 3),
#         Album(8, 'I Put a Spell on You', 1965, 4),
#         Album(9, 'Baltimore', 1978, 4),
#         Album(10, 'Here Comes the Sun', 1971, 4),
#         Album(11, 'Fodder on My Wings', 1982, 4),
#         Album(12, 'Ring Ring', 1973, 2),
#     ]