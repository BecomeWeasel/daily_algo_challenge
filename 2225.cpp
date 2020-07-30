#include <string.h>

#include <iostream>
#include <vector>

using namespace std;

#define BORDER_MAX 201
#define MODULO 1000000000

int N, K;
int dp[BORDER_MAX][BORDER_MAX];

int ans();

int main(void) {
  cin >> N >> K;
  cout << ans();
}

int ans() {
  memset(dp, 0, sizeof(dp));

  for (int i = 0; i <= N; i++) {
    dp[i][1] = 1;
  }

  for (int i = 2; i <= K; i++) {
    for (int j = 0; j <= N; j++) {
      for (int h = 0; h <= j; h++) {
        dp[j][i] = (dp[j][i] % MODULO + (dp[h][i - 1]) % MODULO) % MODULO;
      }
    }
  }

  return dp[N][K];
}
