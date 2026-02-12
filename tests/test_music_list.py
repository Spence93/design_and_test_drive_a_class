from lib.music_list import MusicHistory

"""
When class initialised, check empty list is created
"""
def test_list_is_initialised():
    history = MusicHistory()
    expected = []

    assert history.track_list == expected