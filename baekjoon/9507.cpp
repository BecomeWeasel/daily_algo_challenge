#include <iostream>

using namespace std;

#define NMAX 68

long long dp[68];
int n;

long long ans();

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int test_num;
  cin >> test_num;

  while (test_num--) {
    cin >> n;
    cout<<ans()<<'\n';
  }
}

long long ans(){
  dp[0]=dp[1]=1;
  dp[2]=2;
  dp[3]=4;
  for(int i=4;i<=n;i++){
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4];
  }
  return dp[n];
}
