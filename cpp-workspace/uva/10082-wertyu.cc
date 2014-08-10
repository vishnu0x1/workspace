#include <iostream>
#include <cstdio>

using namespace std;

#define gc getchar_unlocked

const char* key_order = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";

int* build_table()
{
  int* dict = new int[256];
  for (int i = 0; i < 256; i++)
    dict[i] = i;
  for (int i = 0; key_order[i]; i++)
    dict[key_order[i + 1]] = key_order[i];
  return dict;
}

const char* convert(const char* str, int* dict)
{
  const char* const begin = str;
  while(*str++);
  char* translated = new char[str - begin];
  str = begin;
  while(*str) *translated++ = dict[*str++];
  *translated = '\0';
  return translated - str + begin;
}

int main()
{
  int* dict = build_table();
  char* str = new char[1 << 20];
  char* s = str;
  while ((*s++ = gc()) != EOF);
  *s = '\0';
  cout << convert(str, dict);
  return 0;
}
