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
    AlbumSet getAlbums();
    void addAlbum(std::string album);
    void removeAlbum(std::string album);
    SongSet getSongs(std::string album);
    void addSong(std::string album, std::string song);
//    void removeSong(std::string album_name, std::string song_name);
    void print();
    friend std::ostream& operator<<(std::ostream& os, const Album& a);
};
#endif
