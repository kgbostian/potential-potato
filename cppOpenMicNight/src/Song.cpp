#ifndef __SONG_CPP__
#define __SONG_CPP__
#include "Song.h"
Song::Song(std::string name)
{
    this->name = name;
};

int Song::getCount()
{
    return count;
}

bool Song::operator<(const Song &rhs) const
{
    bool result = getName().c_str() < rhs.getName().c_str();
    return result;
}


std::ostream& operator<<(std::ostream& os, const Song& s)
{
    os << s.getName().c_str();
    return os;
}

#endif




