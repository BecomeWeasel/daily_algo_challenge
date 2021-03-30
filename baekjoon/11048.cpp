#include <iostream>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 1001

int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
int dp[MAP_SIZE_MAX][MAP_SIZE_MAX];

int dx[3] = {1, 0, 1};
int dy[3] = {0, 1, 1};

int N, M;

int ans();

int main(void) {
  cin >> N >> M;

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      cin >> map[i][j];
    }
  }
  int k = 3;

  cout << ans();
}

int ans() {

  // int dp[MAP_SIZE_MAX][MAP_SIZE_MAX];
  // vector<vector<int>> dp(MAP_SIZE_MAX,vector<int>(MAP_SIZE_MAX,0));  
  
  dp[1][1] = map[1][1];

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      // 목적지까지 계산이 끝났을때
      if (i == N && j == M) break;

      for (int k = 0; k < 2; k++) {
        int ny = i + dy[k];
        int nx = j + dx[k];

        // 보드의 범위를 벗어나는 움직임일때
        if (ny > N || nx > M) continue;

        dp[ny][nx] = max(dp[ny][nx], dp[i][j] + map[ny][nx]);
      }
    }
  }

  // non-reachable
  return dp[N][M];
}