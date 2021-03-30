#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAP_MAX 301

int N, M;
int map[MAP_MAX][MAP_MAX];

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
  int dp[MAP_MAX][MAP_MAX] = {
      0,
  };
  int max_src = 0;

  dp[1][1] = map[1][1];
  max_src = max(max_src, dp[1][1]);

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      dp[i][j]=max(dp[i][j],dp[i-1][j]+map[i][j]);
      dp[i][j]=max(dp[i][j],dp[i][j-1]+map[i][j]);

      max_src=max(max_src,dp[i][j]);
      
    }
  }

  return max_src;
}
