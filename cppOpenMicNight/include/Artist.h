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
    std::string getName(){return name;};
    void addAlbum(std::string album);
    AlbumSet getAlbums();
//    void addSong(std::string song);
//    void removeSong(std::string album_name, std::string song_name);
//    void removeAblum(std::string &album);
    void print();
};
#endif
