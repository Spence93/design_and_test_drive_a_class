from lib.music_list import MusicHistory
import pytest
"""
When class initialised, check empty list is created
"""
def test_list_is_initialised():
    history = MusicHistory()
    expected = []

    assert history.track_list == expected

def test_add_track_as_string():
    history = MusicHistory()
    history.add_track('song1')
    history.add_track('song2')
    history.add_track('song3')

    expected = ['song1', 'song2', 'song3']
    assert history.track_list == expected

def test_add_track_isnt_string():
    history = MusicHistory()

    with pytest.raises(TypeError) as error:
        history.add_track(5)
    error_message = str(error.value)
    assert error_message == "Song must be a string"

