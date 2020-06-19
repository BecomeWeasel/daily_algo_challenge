#include <iostream>
#include <vector>

using namespace std;

int ans();

int num;

vector<int> dp(10001, 0);
vector<int> wine_cost(10001, 0);

int main() {
  cin >> num;
  for (int i = 1; i <= num; i++) {
    int tmp;
    cin >> tmp;
    wine_cost[i] = tmp;
  }
  cout << ans();
}

int ans() {
  dp[1] = wine_cost[1];
  dp[2] = dp[1] + wine_cost[2];

  for (int i = 3; i <= num; i++) {
    dp[i] = max(max((dp[i - 2] + wine_cost[i]), (dp[i - 1])),
                (dp[i - 3] + wine_cost[i - 1] + wine_cost[i]));
  }

  return dp[num];
}