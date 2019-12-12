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
    std::cout << "Removing song: " << song.getName() << std::endl;
    SongSet::iterator si = song_list.find(song);
    std::cout << "After the song_list.find()" << std::endl;
    std::cout << "si = " << (*si).getName() << std::endl;
    //int x = song_list.erase(*si);
    //print();
    //int x = song_list.erase(song);
    print();
    //std::cout << x << " items removed from the set." << std::endl;
};

SongSet Album::getSongList()
{
    return song_list;
};

void Album::print()
{
    SongSet::iterator it;
    std::cout << "Album contains:";
    for (it=song_list.begin(); it!=song_list.end(); ++it)
        std::cout << ' ' << (*it) << std::endl;
    std::cout << '\n'; 
};
#endif
