#include <iostream>
#include <vector>

using namespace std;

int steps;
vector<int> step_point(301);
vector<vector<int> > dp;
// dp[2][1] : 2번째 계단을 오를때 1칸만 오른 상태
// dp[4][2] : 4번째 계단에 오를때 2연속으로 1칸 오른상태
vector<int> step_count(301, 0);

int ans();

int main(void) {
  cin >> steps;
  vector<int> zero_step(3);
  dp.push_back(zero_step);
  for (int i = 1; i <= steps; i++) {
    int tmp;
    cin >> tmp;
    step_point[i] = tmp;

    vector<int> step(3);
    dp.push_back(step);
  }
  cout << ans();
}

int ans() {
  dp[1][1] = step_point[1];
  if (steps >= 2) {
    dp[2][2] = dp[1][1] + step_point[2];
    dp[2][0] = step_point[2];
  }
  for (int i = 3; i <= steps; i++) {
    dp[i][0] =
        max(max(dp[i - 2][0], dp[i - 2][1]),dp[i-2][2]) + step_point[i];
    dp[i][1] = dp[i - 1][0] + step_point[i];
    // dp[i][2] = dp[i - 1][1] + step_point[i];
  }
  return max(max(dp[steps][0], dp[steps][1]), dp[steps][2]);
}