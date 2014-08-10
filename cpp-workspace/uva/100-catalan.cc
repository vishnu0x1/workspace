#include <iostream>
#include <cstdio>

#define LIM 1000000

using namespace std;

int a[LIM] = { 0, 1 }; // a[0] = invalid case, a[1] = 1, base case

int cycle_length(unsigned int n) {
  if (n < LIM && a[n])
    return a[n];

  unsigned int next_n = n & 1 ? (3*n + 1) : n >> 1;
  int len =  cycle_length(next_n) + 1;

  if (n < LIM)
    a[n] = len;

  return len;
}

void swap(int& i, int& j) {
  i = i ^ j;
  j = i ^ j;
  i = i ^ j;
}

int main() {
  int i, j;
  bool swapped;
  while (cin >> i >> j) {

    swapped = false;
    
    // swap (i,j) if i > j
    if (i > j) {
      swap(i, j);
      swapped = true;
    }

    int max_cycle_len = 0;
    for (int k = i; k <= j; k++) {
      int len = cycle_length(k);
      if (max_cycle_len < len)
	max_cycle_len = len;
    }

    if (swapped) swap(i, j);
    cout << i << " " << j << " " << max_cycle_len << endl;
  }
  return 0;
}
