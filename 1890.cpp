#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 100

int map[N_MAX][N_MAX];

int N;

long long ans();

int main(void) {
  cin >> N;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> map[i][j];
    }
  }

  cout << ans();
}

long long ans() {
  long long dp[N_MAX][N_MAX] = {0};
  dp[0][0] = 1;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (i == N - 1 && j == N - 1) break;
      int nx = j + map[i][j];

      if (nx < N) {
        dp[i][nx] += dp[i][j];
      }

      int ny = i + map[i][j];

      if (ny < N) {
        dp[ny][j] += dp[i][j];
      }
    }
  }
  return dp[N - 1][N - 1];
}