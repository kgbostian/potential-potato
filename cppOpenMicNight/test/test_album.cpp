#include "Album.h"
#include "gtest/gtest.h"

TEST(AlbumTests, DefaultAlbum)
{
    Album a = Album("New Album");
    ASSERT_STREQ("New Album", a.getName().c_str());
};


TEST(AlbumTests, DISABLED_AddSongs)
{
    Album a = Album("Add Songs Album");
    Song s = Song("Adding Song");
    a.addSong(s);
    std::list<Song> sl = a.getSongList();
    ASSERT_EQ(1,sl.size());
};
