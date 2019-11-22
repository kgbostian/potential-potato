class Band:
    def __init__(self, name = ""):
        self.__songs = []
    
    def add_song(self, song):
        try:
            self.__songs.append(song)
        except:
            raise
        return None

    def remove_song(self, song):
        try:
            self.__songs.remove(song)
        except:
            raise
        return None

    def get_songs(self):
        return self.__songs

class Song:
    def __init__(self, name = ""):
        self.name = name
        self.requests = 0
        self.notes = ["No New Notes"]
        return None


