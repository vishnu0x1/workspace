#include <iostream>
#include <algorithm>
#include <string>

#define ull unsigned long long

using namespace std;

int* factoradic(int n, ull k)
{
  int* f = new int[n];
  for (int i = 1; i <= n; i++) {
    f[n - i] = k % i;
    k /= i;
  }
  return f;
}

string perm(int n, int* f, string seq)
{
  char* perm = new char[n];
  for (int i = 0; i < n; i++) {
    string::iterator it = seq.begin() + f[i];
    perm[i] = *it;
    seq.erase(it);
  }
  return string(perm, n);
}

int main()
{
  int nr_tests;  
  cin >> nr_tests;

  while (nr_tests--) {
    int n;
    ull k;
    string seq;

    cin >> seq >> k;
    n = seq.length();
    int* f = factoradic(n, k);
    sort(seq.begin(), seq.end());
    cout << perm(n, f, seq) << "\n";
  }

  return 0;
}
