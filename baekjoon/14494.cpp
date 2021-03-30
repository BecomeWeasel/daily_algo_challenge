#include <string.h>

#include <iostream>

using namespace std;

#define MODULO 1000000007

int n, m;

#define MAP_SIZE_MAX 1001

int dp[MAP_SIZE_MAX][MAP_SIZE_MAX];

int ans();

int main(void) {
  cin >> n >> m;
  cout << ans();
}

int ans() {
  memset(dp, 0, sizeof(dp));

  dp[1][1] = 1;

  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
      dp[i][j] += ((dp[i - 1][j] % MODULO + dp[i][j - 1] % MODULO) % MODULO +
                   dp[i - 1][j - 1] % MODULO) %
                  MODULO;
    }
  }

  return dp[m][n];
}
