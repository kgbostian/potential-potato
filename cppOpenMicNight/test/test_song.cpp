#include "Song.cpp"
#include "gtest/gtest.h"

TEST(SongTest, Defaults)
{
    Song newSong("Test Song");
    EXPECT_EQ(0, newSong.getCount());
    EXPECT_STREQ("Test Song", newSong.getName().c_str());
}



TEST(SongTest, CountIncr)
{
    Song newSong("CountIncr");
    newSong.incrementCount();
    EXPECT_EQ(1, newSong.getCount());
}
