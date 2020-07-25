#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 16

int N, M, K;

long long ans();

int main(void) {
  cin >> N >> M >> K;
  cout << ans();
}

long long ans() {
  int dp[MAP_SIZE_MAX][MAP_SIZE_MAX] = {
      0,
  };
  dp[1][1] = 1;

  // 동그라미가 있을때
  int cnt = 1;
  if (K != 0) {
    int xpos, ypos;

    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= M; j++) {
        if (cnt++ == K) {
          ypos = i;
          xpos = j;
          break;
        }
      }
    }

    for (int i = 1; i <= ypos; i++) {
      for (int j = 1; j <= xpos; j++) {
        if (i == 1 && j == 1) {
          continue;
        }
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
      }
    }

    int point = dp[ypos][xpos];

    memset(dp, 0, sizeof(dp));

    
    dp[ypos][xpos] = 1;

    for (int i = ypos; i <= N; i++) {
      for (int j = xpos; j <= M; j++) {
        if (i == ypos && j == xpos) continue;
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
      }
    }

    return 1LL * point * dp[N][M];

  }
  // 동그라미가 없을때
  else {
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= M; j++) {
        if (i == 1 && j == 1) continue;
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
      }
    }

    return 1LL * dp[N][M];
  }
}
