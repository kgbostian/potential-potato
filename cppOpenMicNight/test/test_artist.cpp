#include "Artist.h"
#include "gtest/gtest.h"

TEST(ArtistTests, DefaultArtist)
{
    Artist a = Artist("New Artist");
    ASSERT_STREQ("New Artist", a.getName().c_str());
};


TEST(ArtistTests, AddSongs)
{
//    Artist a = Artist("Artist A");
//    std::string an = "Album 1";
//    Song s1 = Song("Song A");
//    Song s2 = Song("Song C");
//    Song s3 = Song("Song B");
//    a.addAlbum(an);
//    a.addSong(an, s1);
//    SongSet songs = a.getSongs();
//    ASSERT_EQ(1,songs.size());
//    a.addSong(an, s2);
//    songs = a.getSongs();
//    ASSERT_EQ(2,songs.size());
//    a.addSong(an, s3);
//    songs = a.getSongs();
//    ASSERT_EQ(3,songs.size());
};

TEST(ArtistTests, RemoveSongs)
{
    //Artist a = Artist("Add Songs Artist");
    //Song s1 = Song("Song One");
    //Song s2 = Song("Song Two");
    //a.addSong(s1);
    //SongSet songs = a.getSongs();
    //ASSERT_EQ(1,songs.size());
    //a.removeSong(s1);
    //songs = a.getSongs();
    //ASSERT_EQ(0,songs.size());
};
