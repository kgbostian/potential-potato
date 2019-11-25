#ifndef __ALBUM_CPP__
#define __ALBUM_CPP__
#include "Album.h"

Album::Album(std::string name)
{
   this->name = name;
};

void Album::addSong(Song &song)
{
    song_list.insert(song);
};

std::set<Song> Album::getSongList()
{
    return song_list;
};
#endif
