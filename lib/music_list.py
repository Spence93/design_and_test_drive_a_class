class MusicHistory():
    def __init__(self):
        self.track_list = []

    def add_track(self, song):
        if not isinstance(song, str):
            raise TypeError("Song must be a string")
        self.track_list.append(song)

    def get_tracks(self):
        return list(self.track_list)    