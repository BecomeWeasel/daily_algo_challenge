#include <iostream>
using namespace std;

#define N_MAX 101

int V[NMAX];
int N, S, M;

int ans();

int main(void) {
  cin >> N >> S >> M;
  for (int i = 1; i <= N; i++) {
    cin >> V[i];
  }

  cout << ans();
}

int ans() {
  int dp[N_MAX][2] = {-1};

  
  return (dp[N][0] == -1) && (dp[N][1] == -1) ? -1 : max(dp[N][0], dp[N][1]);
}