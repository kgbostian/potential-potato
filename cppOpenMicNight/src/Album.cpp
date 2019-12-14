#ifndef __ALBUM_CPP__
#define __ALBUM_CPP__
#include "Album.h"

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

bool Album::operator<(const Album &rhs) const
{
    bool result = getName() < rhs.getName();
    return result;
}

std::ostream& operator<<(std::ostream& os, const Album& a)
{
    os << a.getName().c_str();
    return os;
}
void Album::print()
{
    SongSet::iterator it;
    std::cout << "Album contains:" << std::endl;
    for (it=song_list.begin(); it!=song_list.end(); ++it)
        std::cout << ' ' << *it << std::endl;
    std::cout << '\n'; 
};
#endif
