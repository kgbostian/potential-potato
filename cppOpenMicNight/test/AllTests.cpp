#include <gtest/gtest.h>
#include "test_album.cpp"
#include "test_song.cpp"

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
