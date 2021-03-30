#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 1001
#define INF 987654321

int map[N_MAX];
int N;

int ans();

int main(void) {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    cin >> map[i];
  }
  cout << ans();
}

int ans() {
  vector<int> dp(N_MAX,INF);
  dp[1]=0;

  for (int i = 1; i <= N; i++) {
    for (int j = map[i]; j > 0; j--) {
      if (i + j <= N) {
        dp[i + j] = min(dp[i + j], dp[i] + 1);
      }
    }
  }

  return dp[N] == INF ? -1 : dp[N];
}