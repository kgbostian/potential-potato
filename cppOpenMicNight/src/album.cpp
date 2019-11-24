#include "album.h"

Album::Album()
{};

Album::addSong(Song song)
{
    songlist.insert(song);
    songlist.sort(); 
};
