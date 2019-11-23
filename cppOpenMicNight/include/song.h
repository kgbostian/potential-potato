#ifndef __SONG__
#define __SONG__

#include <string>
 
class Song
{
    std::string name;
    int count = 0;
    int request_count = 0;
  public:
    Song(std::string name);
    int getCount() {return count;};
    void incrementCount(){count++;};
    int getRequestCount(){return request_count;};
    void incrementRequestCount(){request_count++;};
    std::string getName(){return name;};
    void setName(std::string name){this->name = name;};
};
#endif
