#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int transform[] = {0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 
		   5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2};

void print(string name, string code)
{
  cout << "         " << left << setw(25) << name << code << "\n";
}

int main()
{
  string name;
  string code;

  print("NAME", "SOUNDEX CODE");
  while (cin >> name) {
    int i = 0;
    int last; // first initialized inside the for loop
    code = "0000";
    for (string::iterator it = name.begin(); it != name.end() && i < 4; ++it) {
      int curr = transform[*it - 65];
      if (!i || curr && last != curr) {	
	code[i++] = curr + 48;
      }
      last = curr;
    }
    code[0] = name[0];
    print(name, code);
  }
  cout << "                   END OF OUTPUT" << "\n";
  return 0;
}
