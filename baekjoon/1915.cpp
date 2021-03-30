#include <string.h>

#include <iostream>
#include <vector>

using namespace std;

#define BOARD_SIZE_MAX 1001

int N, M, answer;
int dp[BOARD_SIZE_MAX][BOARD_SIZE_MAX];

int map[BOARD_SIZE_MAX][BOARD_SIZE_MAX];

int ans();

int main(void) {
  memset(dp, 0, sizeof(dp));
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < M; j++) {
      map[i][j] = dp[i][j] = s[j] - '0';
      if (map[i][j] == 1) {
        answer = 1;
      }
    }
  }

  cout << ans();
}

int ans() {
  for (int i = 1; i < N; i++) {
    for (int j = 1; j < M; j++) {
      if (map[i - 1][j - 1] == 1 && map[i - 1][j] == 1 && map[i][j - 1] == 1) {
        dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
        answer = max(answer, dp[i][j]);
      }
    }
  }

  return answer * answer;
}