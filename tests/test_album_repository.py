from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    # Assert on the results
    # To pass, remove the unrequired seeds (to save a lot of typing).
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2)
    ]

def test_album_title(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums[0].title == "Doolittle"

def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Test Album", 2000, 1))

    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, "Test Album", 2000, 1),
    ]

    assert result[-1] == Album(5, "Test Album", 2000, 1) # My test - more specific as it checks that the last (newest) record is equal to the one we have added.

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(1)

    albums = repository.all()
    assert albums == [
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
    ]

    assert (album.id != 1 for album in albums) # My test - more specific as it checks that the removed id does not exist.

def test_delete_nonexistent_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums_before = repository.all()

    repository.delete(999)

    albums_after = repository.all()

    albums = repository.all()
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
    ] # My test - makes sure that the attempted deletion of a nonexistent record has no effect on the database.

    assert albums_after == albums_before # My test - makes sure that the database is consistent before and after the attempted deletion.

def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(4)
    assert album == Album(4, 'Super Trouper', 1980, 2)

    album = repository.find(999)
    assert album == None
