#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define MAX 101
#define W_MAX 100001

vector<vector<int>> dp(MAX, vector<int>(W_MAX, 0));
vector<int> weight(MAX);
vector<int> cost(MAX);
int N, K;

int ans();

int main(void) {
  cin >> N >> K;
  for (int i = 1; i <= N; i++) {
    cin >> weight[i] >> cost[i];
  }
  cout << ans();
}

int ans() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= K; j++) {
      if (weight[i] >j) {
        dp[i][j] = dp[i - 1][j];
      } else {
        dp[i][j] = max(dp[i - 1][j], dp[i-1][j - weight[i]] + cost[i]);
      }
    }
  }

  // for (int i = 1; i <= N; i++) {
  //   for (int j = 1; j <= K; j++) {
  //     cout << dp[i][j] << " ";
  //   }
  //   cout << endl;
  // }
  // cout << endl;
  // cout << endl;
  // cout << endl;
  return dp[N][K];
}
