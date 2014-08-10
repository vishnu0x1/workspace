#include <iostream>

using namespace std;

int main() {
  int n;
  int a, b, x, y;

  cin >> n;
  while(n--) {
    cin >> x >> y;
    a = (x + y) >> 1;
    b = (x - y) >> 1;
    if (a >= 0 && b >= 0 && a + b == x)
      cout << a << " " << b << "\n";
    else
      cout << "impossible\n";
  }

  return 0;
}
