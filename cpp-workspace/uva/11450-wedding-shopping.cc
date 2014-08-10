
#include <cstring>
#include <iostream>
#include <algorithm>

#define MAX_MONEY 200
#define MAX_NR_GARMENTS 20
#define MAX_NR_MODELS 20

using namespace std;

int dp[MAX_MONEY + 1][MAX_NR_GARMENTS + 1];
int cost[MAX_NR_GARMENTS][MAX_NR_MODELS];
int K[MAX_NR_GARMENTS];

int solve(int M, int C) {
  memset(dp, -1, sizeof(dp[0][0]) * (MAX_MONEY + 1) * (MAX_NR_GARMENTS + 1));
  dp[0][0] = 0;  // base case

  int res = -1;
  for (int m = 1; m <= M; m++) {
    for (int c = 1; c <= C; c++) {
      for (int k = 0; k < K[c - 1]; k++) {
	int s, t;
	if (m >= (s = cost[c - 1][k]) && (t = dp[m - s][c - 1]) >= 0) {
	  dp[m][c] = max(dp[m][c], s + t);
	}
      }
    }
    res = max(res, dp[m][C]);
  }
  
  return res;
}

int main() {
  int N, M, C;
  cin >> N;

  while(N--) {
    cin >> M >> C;
    for (int i = 0; i < C; i++) {
      cin >> K[i];
      for (int j = 0; j < K[i]; j++)
	cin >> cost[i][j];
    }

    int res = solve(M, C);
    if (res == -1)  cout << "no solution\n";
    else            cout << res << "\n";
  };

  return 0;
}
