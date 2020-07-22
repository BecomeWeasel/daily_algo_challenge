#include <iostream>
#include <vector>

using namespace std;

#define modulo (10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 + 7)
#define N_MAX 191230

int N;

vector<int> dp(N_MAX, -1);

int ans();

int solve(int n) {
  if (dp[n] != -1)
    return dp[n];
  else {
    dp[n] = (solve(n - 1) % modulo + solve(n - 2) % modulo) % modulo;
    return dp[n];
  }
}

int ans() { return solve(N); }

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int test_num;
  cin >> test_num;
  dp[1] = 1;
  dp[2] = 2;
  while (test_num--) {
    cin >> N;
    cout << ans() << '\n';
  }
}
