from user import User


class Artist(User):
    _songs = {}
    _playlist = []
    _ratings = []
    _currentRating = 0

    def _add_song(self, song):
        self._songs.append(song)
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
