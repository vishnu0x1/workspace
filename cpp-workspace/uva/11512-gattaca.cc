
#include <cstdio>
#include <iostream>

#define gc getchar_unlocked
#define pc putchar_unlocked

#define MAX_LEN 1000
#define RADIX 4

using namespace std;

void print(int* a, int n) {
  for (int i = 0; i < n; i++) cout << a[i] << " ";
  cout << endl;
}

inline bool leq(int a1, int a2, int b1, int b2)
{
  return a1 < b1 || a1 == b1 && a2 <= b2;
}

inline bool leq(int a1, int a2, int a3, int b1, int b2, int b3)
{
  return a1 < b1 || a1 == b1 && leq(a2, a3, b2, b3);
}

void radix_pass(int* a, int* b, int* r, int n, int K)
{
  int* c = new int[K + 2]();   // K + 1 digits
  for (int i = 0; i < n; i++)  c[r[a[i]] + 1]++;
  for (int i = 0; i < K; i++)  c[i + 1] += c[i];
  for (int i = 0; i < n; i++)  b[c[r[a[i]]]++] = a[i];
  delete[] c;
}

void suffix_array(int* s, int* SA, int n, int K)
{
  int n0 = (n+2)/3, n1 = (n+1)/3, n2 = n/3, n02 = n0 + n2;
  
  int* s12 = new int[n02 + 3]();
  int* SA12 = new int[n02 + 3]();
  int* s0 = new int[n0];
  int* SA0 = new int[n0];

  for (int i = 0, j = 0; i < n + (n0 - n1); i++) if (i % 3) s12[j++] = i;

  radix_pass(s12, SA12, s+2, n02, K);
  radix_pass(SA12, s12, s+1, n02, K);
  radix_pass(s12, SA12, s,   n02, K);

  int name = 0;
  int c0 = -1, c1 = -1, c2 = -1;
  for (int i = 0; i < n02; i++) {
    int z = SA12[i];
    if (s[z] != c0 || s[z + 1] != c1 || s[z + 2] != c2) {
      name++;
      c0 = s[z], c1 = s[z + 1], c2 = s[z + 2];
    }
    if (z % 3 == 1) s12[z/3]      = name;
    else            s12[z/3 + n0] = name;
  }

  if (name < n02) {
    suffix_array(s12, SA12, n02, name);
    for (int i = 0; i < n02; i++)  s12[SA12[i]] = i + 1;
  } else {
    for (int i = 0; i < n02; i++)  SA12[s12[i] - 1] = i;
  }
  for (int i = 0, j = 0; i < n02; i++) if (SA12[i] < n0) s0[j++] = SA12[i] * 3;
  radix_pass(s0, SA0, s, n0, K);

  for (int p = 0, t = n0 - n1, k = 0; k < n; k++) {
    int z = SA12[t];

#define GetI() (z < n0 ? 3*z + 1 : 3*(z - n0) + 2)

    if (t == n02) {
      SA[k] = SA0[p++];
    } 
    else if (p == n0) {
      z = SA12[t++]; SA[k] = GetI();
    } 
    else {
      int i = GetI();
      int j = SA0[p];
    
      if (z < n0 ? leq(s[i], s12[z + n0], s[j], s12[j/3]) : 
	  leq(s[i], s[i + 1], s12[z - n0 + 1], s[j], s[j + 1], s12[j/3 + n0])) {
	SA[k] = i; t++;
      } 
      else {
	SA[k] = j; p++;
      }
    }
  }

  delete[] s12; delete[] SA12; delete[] s0; delete[] SA0;
}

void height(int* a, int* pos, int* height, int n) 
{
  int* rank = new int[n];
  for (int i = 0; i < n; i++)
    rank[pos[i]] = i;
  int h = 0;
  for (int i = 0; i < n; i++) {
    if (rank[i] > 0) {
      int j = pos[rank[i] - 1];
      while (a[i + h] == a[j + h]) h++;
      height[rank[i]] = h;
      if (h > 0) h--;
    }
  }
  delete[] rank;
}

int main()
{
  int s[MAX_LEN + 3], sa[MAX_LEN + 3], h[MAX_LEN + 3];
  int d[256] = {0};
  int t;

  // d[0] = 0
  d['A'] = 1, d['C'] = 2, d['G'] = 3, d['T'] = 4;
  d[1] = 'A', d[2] = 'C', d[3] = 'G', d[4] = 'T';

  cin >> t; cin.ignore();

  while(t--) {
    int n = 0;
    char c;
    while(d[c = gc()] != 0)
      s[n++] = d[c];

    // compute suffix array
    s[n] = s[n + 1] = s[n + 2] = 0;
    suffix_array(s, sa, n, RADIX);
    height(s, sa, h, n);

    h[0] = -1;
    int max_h = 0, max_ih, max_cnt;
    for (int i = n - 1; i > 0; i--) {
      if (h[i] >= max_h) {
	max_h = h[i]; max_ih = i; max_cnt = 2; 
	while (h[--i] == max_h) ++max_cnt; // never i < 0, sentinel h[0] = -1
	++i;
      }
    }
    
    if (max_h == 0) cout << "No repetitions found!\n";
    else {
      for (int i = 0; i < max_h; i++) pc(d[s[sa[max_ih] + i]]);
      cout << " " << max_cnt << "\n";
    }
  }

  return 0;
}
