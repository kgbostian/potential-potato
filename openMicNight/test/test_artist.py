import pytest
from openMicNight.artist import Artist


@pytest.fixture
def artist_creation():
    return Artist("newArtist")
    
def test_artist_add_remove_song(artist_creation):
    song = "(Don't Fear) The Reaper"
    artist = "Blue Oyster Cult"
    data =  {"song": song, "artist": artist}
    artist_creation.add_song(data)
    new_data = artist_creation.get_song_list()
    assert data in new_data
    assert len(new_data) == 1
    artist_creation.remove_song(song)
    assert data not in new_data
    assert len(new_data) == 0
    

def test_artist_add_duplicate_song(artist_creation):
    song = "(Don't Fear) The Reaper"
    artist = "Blue Oyster Cult"
    data =  {"song": song, "artist": artist}
    artist_creation.add_song(data)
    new_data = artist_creation.get_song_list()
    assert data in new_data
    assert len(new_data) == 1
    artist_creation.add_song(data)
    new_data = artist_creation.get_song_list()
    assert data in new_data
    assert len(new_data) == 1


    
