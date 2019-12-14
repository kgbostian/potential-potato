#ifndef __ALBUM_H__
#define __ALBUM_H__
#include <string>
#include <set>
#include "Song.h"

typedef std::set<Song> SongSet;
class Album
{
    std::string name = "";
    SongSet song_list;
  public:
    Album(std::string name);
    void addSong(Song song);
    void removeSong(Song &song);
    std::string getName()const{return name;};
    bool operator<(const Album &rhs) const;
    //virtual bool operator()(const Album &rhs) const;
    SongSet getSongs();
    void print();
};
#endif
