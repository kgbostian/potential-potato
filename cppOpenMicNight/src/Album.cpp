#ifndef __ALBUM_CPP__
#define __ALBUM_CPP__
#include "Album.h"

//struct CustomCompare
//bool operator()(const Song &lhs, const Song &rhs)
//{
//    return lhs.getName().c_str() < rhs.getName().c_str();
//}

Album::Album(std::string name)
{
   this->name = name;
};

void Album::addSong(Song song)
{
    song_list.insert(song);
};

void Album::removeSong(Song &song)
{
    song_list.erase(song);
};

SongSet Album::getSongs()
{
    return song_list;
};

void Album::print()
{
    SongSet::iterator it;
    std::cout << "Album contains:" << std::endl;
    for (it=song_list.begin(); it!=song_list.end(); ++it)
        std::cout << ' ' << (*it) << std::endl;
    std::cout << '\n'; 
};
#endif
