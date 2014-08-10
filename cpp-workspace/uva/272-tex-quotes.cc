#include <iostream>
#include <cstdio>

#define gc getchar_unlocked
#define START_QUOTE "``"
#define END_QUOTE "\'\'"

using namespace std;

int main() {
  char s;
  bool begin = true;
  while ((s = gc()) != EOF) {
    if (s == '\"') {
      cout << (begin ? START_QUOTE : END_QUOTE);
      begin = !begin;
    }
    else
      cout << s;
  }
  return 0;
}
