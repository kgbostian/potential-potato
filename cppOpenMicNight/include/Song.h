#ifndef __SONG__
#define __SONG__

#include <string>
#include <iostream>
 
class Song
{
    std::string name;
    mutable int count = 0;
    mutable int request_count = 0;
  public:
    Song(std::string name);
    bool operator<(const Song &rhs) const;
    //bool operator()(const Song &lhs, const Song &rhs);
    bool operator()(const Song &rhs) const;
    friend std::ostream& operator<<(std::ostream &os, const Song& s);
    int getCount();
    void incrementCount(){count++;};
    int getRequestCount(){return request_count;};
    void incrementRequestCount(){request_count++;};
    std::string getName() const {return name;};
    void setName(std::string name){this->name = name;};
};
#endif
