#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

class snail {
  int h, u, d;
  float f;
  int m, m2;

public:
  snail(int, int, int, float);
  int solve();
};

snail::snail(int h, int u, int d, float f) {
  this->h = h;
  this->u = u;
  this->d = d;
  this->f = f / 100;
}

int snail::solve() {
  int n = 1;
  float climb = u;
  float ht = u;

  while(ht >= d && ht <= h) {
    n++;
    climb -= u*f;
    if (climb < 0)  climb = 0;
    ht += climb - d;
  }

  return ht < d ? -n : n;
}

int main() {
  int h, u, d, f;
  while (true) {
    cin >> h >> u >> d >> f;
    if (!h)  break;
    snail s(h, u, d, f);
    int n = s.solve();
    if (n > 0)
      cout << "success on day " << n << "\n";
    else 
      cout << "failure on day " << -n << "\n";
  }
  return 0;
}
