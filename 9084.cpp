#include <string.h>

#include <iostream>
#include <vector>

using namespace std;

#define MONEY_MAX 10001

int N;

int ans();

int main(void) {
  int test_num;
  cin >> test_num;

  while (test_num--) {
    cin >> N;
    cout << ans() << '\n';
  }
}

int ans() {
  int coin[N];
  memset(coin, 0, sizeof(coin));
  for (int i = 0; i < N; i++) {
    cin >> coin[i];
  }
  int target_money;
  cin >> target_money;

  int dp[MONEY_MAX];
  memset(dp, 0, sizeof(dp));

  dp[0]=1;

  for(int i=0;i<N;i++){
    for(int j=coin[i];j<=target_money;j++){
      dp[j]+=dp[j-coin[i]];
    }
  }


  return dp[target_money];
}