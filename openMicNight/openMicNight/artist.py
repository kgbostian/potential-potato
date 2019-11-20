from openMicNight.user import User


class Artist(User):
    _songs = []
    _playlist = []
    _ratings = []
    _currentRating = 0

    def get_info(self):
        print(
            "Songs: {self._songs}\
               Playlist: {self._playlist}\
               Ratings: {self._ratings}\
               CurrentRating: {self._currentRating}"
        )
        return None

    def _add_song(self, data):
        self._songs.append(data["song"])
        return None

    def _remove_song(self, song):
        try:
            self._songs.remove(song)
            self._playlist.remove(song)
            return None
        except Exception as err:
            raise err

    def _add_to_playlist(self, song):
        try:
            # bisect.insort(_playlist, song)
            return None
        except Exception as err:
            raise err

    def _remove_from_playlist(self, song):
        try:
            self._playlist.remove(song)
            return None
        except Exception as err:
            raise err
