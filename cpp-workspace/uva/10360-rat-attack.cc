#include <iostream>
#include <algorithm>

#define GRID_SIZE 1025

using namespace std;

struct point {
  int x, y;
};

int a[GRID_SIZE][GRID_SIZE];  // manhattan grid

point max_neighbor_count() {
  int max_count = -1;
  point pt;
  for (int i = 0; i < GRID_SIZE; i++) {
    for (int j = 0; j < GRID_SIZE; j++) {
      if (a[i][j] > max_count) {
				max_count = a[i][j];
				pt.x = i; pt.y = j;
      }
    }
  }
  return pt;
}

inline void spread_impact(point& pt, int d, int pop_size) {
  int minx, maxx, miny, maxy;
  minx = max(0, pt.x - d); maxx = min(pt.x + d, GRID_SIZE - 1);
  miny = max(0, pt.y - d); maxy = min(pt.y + d, GRID_SIZE - 1); 
  for (int i = minx; i <= maxx; i++)
    for (int j = miny; j <= maxy; j++)
      a[i][j] += pop_size;
}

int main() {
  int nr_scenarios;
  int d, n, size, max_count;
  point pt, max_node;

  cin >> nr_scenarios;
  while (nr_scenarios--) {
    cin >> d >> n;
    fill_n(&a[0][0], GRID_SIZE * GRID_SIZE, 0);
    while (n--) {
      cin >> pt.x >> pt.y >> size;
      spread_impact(pt, d, size);
    }
    max_node = max_neighbor_count();
    max_count = a[max_node.x][max_node.y];
    cout << max_node.x << " " << max_node.y << " "  << max_count << "\n";
  }

  return 0;
}
  
