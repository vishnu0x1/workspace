
#include <iostream>
#include <string>

#define min(a, b) (a < b ? a : b)

using namespace std;

struct point {
  int x, y;

  friend istream &operator>>(istream& in, point& p) {
    in >> p.x >> p.y;
    return in;
  }
};

struct line {
  point p1, p2;

  line(point& p1, point& p2) : p1(p1), p2(p2) {}
};

bool cmp_slope(line& l1, line& l2)
{
  int s = (l1.p2.y - l1.p1.y) * (l2.p2.x - l2.p1.x);
  int t = (l2.p2.y - l2.p1.y) * (l1.p2.x - l1.p1.x);
  return s == t;
}

int sdist(point& p1, point& p2)
{
  int delta_x = p1.x - p2.x;
  int delta_y = p1.y - p2.y;
  return delta_x * delta_x + delta_y * delta_y;
}

bool len_eq(line& l1, line& l2)
{
  return sdist(l1.p1, l1.p2) == sdist(l2.p1, l2.p2);
}

void parallel(line* lines, int N, int& i, int& j)
{
  for (; i < N - 1; i++) {
    for (j = i + 1; j < N; j++) {
      if (cmp_slope(lines[i], lines[j])) return;
    }
  }
  i = j = N;
}

string solve(point& p1, point& p2, point& p3, point& p4)
{
  line lines[] = { line(p1, p2), line(p1, p3), line(p1, p4),
		   line(p2, p3), line(p2, p4),
		   line(p3, p4) };
  
  string result;
  int i, j, k, l;
  const int N = sizeof(lines) / sizeof(lines[0]);
  i = 0;  parallel(lines, N, i, j);
  k = i + 1;  parallel(lines, N, k, l);

  // both pairs of opposite sides are parallel
  if (k < N) {
    int diag = 3 - (i + k);
    bool diag_eq = len_eq(lines[diag], lines[N - diag - 1]);

    if (len_eq(lines[i], lines[j]) &&
	len_eq(lines[j], lines[k]) &&
	len_eq(lines[k], lines[l])) {
      result = diag_eq ? "Square" : "Rhombus";
    }
    else {
      result = diag_eq ? "Rectangle" : "Parallelogram";
    }
  }
  // one pair of opposite sides are parallel
  else if (i < N) {
    result = "Trapezium";
  }
  // no parallel sides
  else {
    result = "Ordinary Quadrilateral";
  }

  return result;
}

int main()
{
  int T;
  cin >> T;

  for (int k = 1; k <= T; k++) {
    point p1, p2, p3, p4;
    cin >> p1 >> p2 >> p3 >> p4;
    cout << "Case " << k << ": " << solve(p1, p2, p3, p4) << "\n";
  }
  
  return 0;
}
