#include <iostream>

using namespace std;

#define N_MAX 91

// dp[i][0] : i자리 이친수중 끝이 0으로 끝나는 것의 개수
// dp[i][1] : i자리 이친수중 끝이 1로 끝나는 것의 개수
long long dp[N_MAX][2];

int N;

long long ans();

int main(void) {
  cin >> N;
  cout << ans();
}

long long ans() {
  dp[1][0] = dp[2][1] = 0;
  dp[1][1] = dp[2][0] = 1;

  for (int i = 3; i <= N; i++) {
    // i-1자리 이친수가 0으로 끝나면
    // i자리의 맨 끝 수는 0 혹은 1
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1];

    // i-1자리 이친수가 1로 끝나면
    // i자리의 맨 끝 수는 무조건 0, 1이면 규칙 2 위배
    dp[i][1] = dp[i - 1][0];
  }

  return (dp[N][0] + dp[N][1]);
}