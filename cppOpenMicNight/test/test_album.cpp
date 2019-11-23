#include "album.h"
#include "gtest/gtest.h"

TEST(AlbumTests, DefaultAlbum)
{
    Album a = Album();
    ASSERT_STREQ("", a.getName().c_str());
};
