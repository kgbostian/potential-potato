#ifndef __ARTIST_CPP__
#define __ARTIST_CPP__
#include "Artist.h"

Artist::Artist(std::string name)
{
   this->name = name;
};

void Artist::addAlbum(std::string album_name)
{
    Album new_album = Album(album_name);
    album_set.insert(new_album);
};

//AlbumSet Artist::getAlbums()
//{
//    return album_set;
//};
//void Artist::addSong(std::string album_name, std::string song_name)
//{
//    AlbumSet::iterator ai = album_list.find(album_name)
//    Song song = Song(song_name)
//    ai->addSong(song)
//};
//
//void Artist::removeSong(std::string albumn_name, std::string song_name)
//{
//    AlbumSet::iterator ai = album_list.find(album_name);
//    ai->removeSong(song_name);
//};
//
//void Artist::removeSong(std::string albumn_name, std::string song_name)
//{
//    AlbumSet::iterator ai = album_list.find(album_name);
//    ai->removeSong(song_name);
//};

void Artist::print()
{
    //AlbumSet::iterator it;
    //std::cout << "Artist contains:" << std::endl;
    //for (it=album_set.begin(); it!=album_set.end(); ++it)
    //    std::cout << ' ' << (*it).print() // << std::endl;
    //std::cout << '\n'; 
};
#endif
