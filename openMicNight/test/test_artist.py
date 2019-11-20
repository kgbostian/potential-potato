import pytest
from openMicNight.artist import Artist


@pytest.fixture
def artist_creation():
    return Artist("newArtist")
    
def test_artist_add_song(artist_creation):
    artist_creation._add_song({"song": "(Don't Fear) The Reaper", "artist": "Blue Oyster Cult"})
    data = artist_creation.get_info()


    
