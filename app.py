from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# Retrieve all albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

print("\n---------------- Artists ---------------------\n")

# List them out
for artist in artists:
    print(artist)

print("\n---------------- Albums ---------------------\n")

for album in albums:
    print(f"{album.title} released {album.release_year}")