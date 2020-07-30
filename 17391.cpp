#include <string.h>

#include <iostream>

using namespace std;

#define MAP_SIZE_MAX 301

int N, M;
int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
int dp[MAP_SIZE_MAX][MAP_SIZE_MAX];

int ans();

int main(void) {
  cin >> N >> M;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      cin >> map[i][j];
    }
  }
  cout << ans();
}

int ans() {
  memset(dp,98765432,sizeof(dp));

  dp[1][1] = 0;

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      if (i == N && j == M) return dp[N][M];

      for (int h = 1; h <= map[i][j]; h++) {
        if (i + h <= N) {
          dp[i + h][j] = min(dp[i + h][j], dp[i][j] + 1);
        }
        if (j + h <= M) {
          dp[i][j + h] = min(dp[i][j + h], dp[i][j] + 1);
        }
      }
    }
  }

  return -1;
}