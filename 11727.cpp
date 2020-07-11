#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 1001

int n;
int d[N_MAX];

int ans();

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n;
  cout << ans();
}

int dp(int target_n) {
  if (target_n == 1) return 1;
  if (target_n == 2) return 3;
  if (target_n == 3) return 5;
  if (d[target_n] != 0) return d[target_n];
  return d[target_n] = (dp(target_n - 2)*2%10007 + dp(target_n - 1))%10007;
}

int ans() { return dp(n); }
