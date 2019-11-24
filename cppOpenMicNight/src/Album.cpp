#ifndef __ALBUM_CPP__
#define __ALBUM_CPP__
#include "Album.h"

Album::Album(std::string name)
{
   this->name = name;
};

void Album::addSong(Song &song)
{
    //songlist.insert(song);
    //songlist.sort(); 
};

std::list<Song> Album::getSongList()
{
    return songList;
};
#endif
