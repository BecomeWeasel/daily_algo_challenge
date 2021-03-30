#include <iostream>
#include <vector>

using namespace std;

int line_num;
int MAX = -1000000000;
vector<vector<int> > cost;
vector<vector<int> > dp;

int ans();

int main(void) {
  cin >> line_num;
  vector<int>l_dp(line_num+1);
  dp.push_back(l_dp);
  for (int i = 1; i <= line_num; i++) {
    vector<int> v(line_num);
    vector<int> l_dp(line_num+1);
    for (int j = 0; j < i; j++) {
      int tmp;
      cin >> tmp;
      v[j] = tmp;
    }
    cost.push_back(v);
    dp.push_back(l_dp);
  }
  cout << ans();
}

int ans() {
  dp[1][0] = cost[0][0];
  for (int i = 2; i <= line_num; i++) {
    for (int j = 0; j < i; j++) {
      if (j - 1 < 0)
        dp[i][j] = dp[i - 1][j];
      else if (j + 1 >= i)
        dp[i][j] = dp[i - 1][j - 1];
      else
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]);

      dp[i][j] += cost[i - 1][j];
    }
  }
  for (int i = 0; i < line_num; i++) {
    MAX = max(MAX, dp[line_num][i]);
  }
  return MAX;
}