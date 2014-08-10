#include <iostream>

using namespace std;

int amperage[20];

int calc_max_amperage(int n, int m, int capacity)
{
  int max_amperage = 0;
  int curr_amperage = 0;
  int device;
  int* state = new int[n]();
  
  for (int i = 0; i < n; i++) {
    cin >> amperage[i];
  }

  for (int i = 0; i < m; i++) {
    cin >> device;
    device--;
    state[device] = 1 - state[device];  // toggle state(0, 1)
    // multiplier = 2 * state - 1
    curr_amperage += (2 * state[device] - 1) * amperage[device];
    if (curr_amperage > max_amperage) max_amperage = curr_amperage;
  }

  return max_amperage;
}

int main()
{
  int i = 0;  // sequence counter
  int n, m, c;  // nr devices, nr toggle operations, fuse capacity  
  
  while(cin >> n >> m >> c) {
    if (!n && !m && !c) break;

    int max_amperage = calc_max_amperage(n, m, c);
    
    cout << "Sequence " << ++i << "\n";
    if (max_amperage > c)
      cout << "Fuse was blown.\n\n";
    else
      cout << "Fuse was not blown.\nMaximal power consumption was "
	   << max_amperage << " amperes.\n\n";
  }
  return 0;
}
