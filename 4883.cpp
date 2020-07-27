#include <string.h>

#include <iostream>

using namespace std;

#define N_MAX 100001
#define INF 100000001

int N;
int dp[N_MAX][5];
int cost[N_MAX][5];

int get_min_among_4(int, int, int, int);

int ans();

int main(void) {
  int test_num = 1;
  int tmp;
  while (true) {
    cin >> N;
    if (N != 0) {
      for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= 3; j++) {
          cin >> cost[i][j];
        }
      }
      cout << test_num++ << ". " << ans() << '\n';
    } else
      break;
  }
}

int ans() {
  memset(dp, INF, sizeof(dp));
  // dp[0][1] = dp[0][2] = dp[0][3] = 0;

  dp[1][2] = cost[1][2];
  dp[1][3] = dp[1][2] + cost[1][3];

  for (int i = 2; i <= N; i++) {
    for (int j = 1; j <= 3; j++) {
      dp[i][j] = get_min_among_4(dp[i - 1][j - 1], dp[i - 1][j],dp[i - 1][j + 1], dp[i][j - 1]);
      dp[i][j] += cost[i][j];
    }
  }
  return dp[N][2];
}

int get_min_among_4(int a, int b, int c, int d) {
  return min(a, min(b, min(c, d)));
}