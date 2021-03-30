#include <string.h>

#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 1001
#define MOD 10007

int N;
int dp[N_MAX][10];

int ans();

int main(void) {
  cin >> N;
  cout << ans();
}

int ans() {
  memset(dp, 0, sizeof(dp));

  for (int i = 0; i <= 9; i++) {
    dp[1][i] = 1;
  }

  for (int i = 2; i <= N; i++) {
    for (int j = 0; j <= 9; j++) {
      for (int k = 0; k <= j; k++) {
        dp[i][j] = (dp[i][j] % MOD + (dp[i - 1][k]) % MOD) % MOD;
      }
    }
  }

  int result = 0;

  for (auto& e : dp[N]) {
    result = (result % MOD + e % MOD) % MOD;
  }

  return result;
}