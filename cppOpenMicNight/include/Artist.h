#ifndef __ARTIST_H__
#define __ARTIST_H__
#include <string>
#include <set>
#include "Album.h"

typedef std::set<Album> AlbumSet;
class Artist
{
    std::string name = "";
    AlbumSet album_set;
  public:
    Artist(std::string name);
//    void addSong(std::string song);
//    void removeSong(std::string album_name, std::string song_name);
//    void addAlbum(std::string album);
//    void removeAblum(std::string &album);
    std::string getName(){return name;};
//    AlbumSet getAlbums();
    void print();
};
#endif
