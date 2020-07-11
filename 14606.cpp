#include <iostream>

using namespace std;

#define N_MAX 11

int dp[N_MAX];
int N;

int ans();

int main(void) {
  cin >> N;
  cout << ans();
}

int ans() {
  fill(dp, dp + N_MAX, 0);
  dp[1] = 0;
  dp[2] = 1;

  // 피자가 n판이 있다고 했을때
  // i 높이와 n-i 높이로 나눠지면
  // 즐거움은 i*(n-i)+dp[i]+dp[n-i]

  for (int i = 3; i <= N; i++) {
    for (int j = i - 1; j >= (float)i / 2; j--) {
      dp[i] = max(dp[i], j * (i - j) + dp[j] + dp[i - j]);
    }
  }

  return dp[N];
}