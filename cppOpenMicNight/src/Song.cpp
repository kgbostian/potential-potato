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
    //std::string a = getName();
    //std::string b = rhs.getName();
    //std::cout << "Operator<: a = " << a.c_str() << " and b = " << b.c_str() << std::endl;
    //bool ab = a < b;
    //std::cout << "A < B = " << ab << std::endl;
    //bool cstr = a.c_str() < b.c_str();
    //std::cout << "A.c_str() < B.c_str() = " << cstr << std::endl;
    bool result = getName() < rhs.getName();
    return result;
}


std::ostream& operator<<(std::ostream& os, const Song& s)
{
    os << s.getName().c_str();
    return os;
}

#endif




