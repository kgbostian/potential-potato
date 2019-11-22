from openmicnight.user import User



class Artist(User):
    __songs = [] 
    __playlist = []
    __ratings = []
    __currentRating = 0

    def add_song(self, data):
        if data["artist"] not in self.__songs:
            self.__songs.append(data["artist"])
            
        
        else:
            #logger.info(f"{data} already exists.")
            print(f"{data} already exists.")
        return None

    def remove_song(self, song):
        try:
            #logger.debug("Attempting to remove {song} from {self.__songs}")
            print(f"Attempting to remove {song} from {self.__songs}")
            self.__songs.remove(song)
            self.__playlist.remove(song)
            return None
        except ValueError as err:
            raise

    def add_to_playlist(self, song):
        try:
            bisect.insort(self.__playlist, song)
            return None
        except Exception as err:
            raise

    def remove_from_playlist(self, song):
        try:
            self.__playlist.remove(song)
            return None
        except Exception as err:
            raise
    
    def get_song_list(self):
       return self.__songs

    def get_playlist(self):
        return self.__playlist
