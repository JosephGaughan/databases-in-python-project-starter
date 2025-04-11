from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
as per the columns in the database
"""
def test_album_constructs():
    album = Album(1, "Title", 1991, 1)
    assert album.id == 1
    assert album.title == "Title"
    assert album.release_year == 1991
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Title", 1991, 1)
    assert str(album) == "Album(1, Title, 1991, 1)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    # your test code goes here! Remove the "pass" afterwards
    album1 = Album(1, "Title", 1991, 1)
    album2 = Album(1, "Title", 1991, 1)
    assert album1.__eq__(album2) == True

def test_albums_are_not_equal():
    # your test code goes here! Remove the "pass" afterwards
    album1 = Album(1, "Title", 1991, 1)
    album2 = Album(2, "Title", 1991, 1)
    assert album1.__eq__(album2) == False

def test_album_format_with_comma():
    album1 = Album(1, "For Emma, Forever Ago", 1991, 1)
    assert album1.__repr__() == "Album(1, For Emma, Forever Ago, 1991, 1)"