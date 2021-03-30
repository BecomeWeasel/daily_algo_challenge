#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 1000

vector<int> dp(N_MAX + 1, 0);
vector<int> p(N_MAX + 1, 0);
int num;

int ans();

int main(void) {
  cin >> num;
  for (int i = 1; i <= num; i++) {
    cin >> p[i];
  }
  cout << ans();
}

int ans() {
  dp[1] = p[1];
  for (int i = 2; i <= num; i++) {
    dp[i] = 987654321;
    for (int j = 1; j <= i; j++) {
      dp[i] = min(dp[i - j] + p[j], dp[i]);
    }
  }

  return dp[num];
}