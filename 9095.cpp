#include <iostream>

using namespace std;

int n;

#define NMAX 11

int dp[NMAX];

int ans();

int main(void) {
  int test_num;
  cin >> test_num;
  while (test_num--) {
    cin >> n;
    cout << ans() << '\n';
  }
}

int ans() {
  fill(dp, dp + NMAX, 0);
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;

  // dp[n]은
  // n=1+n-1 -> 1을 더해서 만들수 있는 개수는 d[n-1]
  // n=2+n-2 -> 2을 더해서 만들수 있는 개수는 d[n-2]
  // n=3+n-3 -> 3을 더해서 만들수 있는 개수는 d[n-3]
  // 1,2,3 더하기 이므로 dp[n]=dp[n-1]+dp[n-2]+dp[n-3]
  for (int i = 4; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  }
  return dp[n];
}