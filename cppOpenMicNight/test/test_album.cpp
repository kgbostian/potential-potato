#include "Album.h"
#include "gtest/gtest.h"

TEST(AlbumTests, DefaultAlbum)
{
    Album a = Album("New Album");
    ASSERT_STREQ("New Album", a.getName().c_str());
};


TEST(AlbumTests, AddSongs)
{
    Album a = Album("Add Songs Album");
    Song s1 = Song("Adding Song");
    Song s2 = Song("Adding Song Two");
    a.addSong(s1);
    std::set<Song> songs = a.getSongList();
    ASSERT_EQ(1,songs.size());
    a.addSong(s2);
    songs = a.getSongList();
    ASSERT_EQ(2,songs.size());
    //std::set<Song>::iterator it;
    //for (it = songs.begin(); it != songs.end(); ++it)
    //{
    //    std::cout << ' ' << *it;
    //    std::cout << '\n';
    //}
};
