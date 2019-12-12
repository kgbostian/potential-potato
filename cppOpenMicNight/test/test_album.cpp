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
    Song s1 = Song("Song A");
    Song s2 = Song("Song C");
    Song s3 = Song("Song B");
    a.addSong(s1);
    SongSet songs = a.getSongList();
    ASSERT_EQ(1,songs.size());
    a.addSong(s2);
    songs = a.getSongList();
    ASSERT_EQ(2,songs.size());
    a.addSong(s3);
    songs = a.getSongList();
    ASSERT_EQ(3,songs.size());
    //a.print();
};

TEST(AlbumTests, RemoveSongs)
{
    Album a = Album("Add Songs Album");
    Song s1 = Song("Song One");
    Song s2 = Song("Song Two");
    a.addSong(s1);
    SongSet songs = a.getSongList();
    ASSERT_EQ(1,songs.size());
    a.removeSong(s1);
    songs = a.getSongList();
    //a.print();
    ASSERT_EQ(0,songs.size());
};
