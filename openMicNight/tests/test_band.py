import pytest
from openmicnight.band import Band, Song

def test_song_default():
    s = Song("Testing Songs")
    assert s.name == "Testing Songs"
    assert s.requests == 0
    assert s.notes[0] == "No New Notes"

@pytest.mark.xfail(reason="Changing __songs objects.")
def test_band_default():
    b = Band("BBQ")
    assert b.get_songs == None
