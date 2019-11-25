#ifndef __ALBUM_H__
#define __ALBUM_H__
#include <string>
#include <set>
#include "Song.h"

class Album
{
    std::string name = "";
    std::set<Song> song_list;
  public:
    Album(std::string name);
    void addSong(Song &song);
    std::string getName(){return name;};
    std::set<Song> getSongList();
};
#endif
