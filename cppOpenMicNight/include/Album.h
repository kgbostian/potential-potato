#ifndef __ALBUM_H__
#define __ALBUM_H__
#include<string>
#include<list>
#include "Song.h"

class Album
{
    std::string name = "";
    std::list<Song> songList;
  public:
    Album(std::string name);
    void addSong(Song &song);
    std::string getName(){return name;};
    std::list<Song> getSongList();
};
#endif
