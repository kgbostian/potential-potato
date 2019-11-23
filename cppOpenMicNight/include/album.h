#include<string>
#include<list>
#include "song.h"

class Album
{
    std::string name = "";
    std::list<Song> songList;
  public:
    void addSong(Song song);
    std::string getName(){return name;};

  private:
    
};
