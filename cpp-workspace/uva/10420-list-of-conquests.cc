#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
  map<string, int> count;
  string country, name;
  int N;

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> country;
    getline(cin, name);

    count[country]++;
  }

  for (map<string, int>::iterator it = count.begin(); it != count.end(); ++it)
    cout << it->first << " " << it->second << "\n";

  return 0;
}
