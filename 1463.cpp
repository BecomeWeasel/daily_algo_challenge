#include <math.h>

#include <iostream>
#include <vector>

using namespace std;

int ans(int);

vector<int> dp((int)pow(10, 6));

int main(void) {
  int num;
  cin >> num;
  cout << ans(num);
  dp[1] = 0;
}

int ans(int num) {
  for (int i = 2; i <= num; i++) {
    dp[i] = dp[i - 1] + 1;
    if (i % 2 == 0) dp[i] = min(dp[i - 1] + 1, dp[i / 2] + 1);
    if (i % 3 == 0) dp[i] = min(dp[i - 1] + 1, dp[i / 3] + 1);
  }
  return dp[num];
}