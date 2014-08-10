
#include <iostream>
#include <limits>

#define MAX_COINS 50
#define imax(a, b) (a > b ? a : b)
#define imin(a, b) (a < b ? a : b)

using namespace std;

int gcd(int a, int b)
{
  return b > 0 ? gcd(b, a % b) : a;
}

int lcm(int a, int b)
{
  return (a * b) / gcd(a, b);
}

void solve(int* T, int n, int length)
{
  int floor = 0;
  int ceil = numeric_limits<int>::max();

  for (int i = 0; i < n - 3; i++) {
    for (int j = i + 1; j < n - 2; j++) {
      int lj = lcm(T[i], T[j]);
      for (int k = j + 1; k < n - 1; k++) {
	int lk = lcm(lj, T[k]);
	for (int l = k + 1; l < n; l++) {
	  int ll = lcm(lk, T[l]);
	  floor = imax(floor, (length / ll) * ll);
	  ceil = imin(ceil, ((length + ll - 1) / ll) * ll);
	}
      }
    }
  }

  cout << floor << " " << ceil << "\n";
}

int main()
{
  int T[MAX_COINS];
  int n, t, length;

  while (cin >> n >> t) {
    if (!n && !t) break;

    for (int i = 0; i < n; i++)
      cin >> T[i];

    for (int i = 0; i < t; i++) {
      cin >> length;
      solve(T, n, length);
    }
  }

  return 0;
}
