#include <string.h>

#include <iostream>

using namespace std;

#define N_MAX 10001
#define MODULO 1000000007

int N, M;
int dp[N_MAX];

int ans();

int main(void) {
  cin >> N >> M;
  cout << ans();
}

int ans() {
  memset(dp, 0, sizeof(dp));
  for (int i = 0; i <= M - 1; i++) {
    // M초의 시간이 없으면
    // 오직 A,AA,AAA,,,, 같은 스킬만 쓸 수 있음
    dp[i] = 1;
  }
  for (int i = M; i <= N; i++) {
    dp[i] = (dp[i - 1] % MODULO + dp[i - M] % MODULO) % MODULO;
  }
  return dp[N];
}