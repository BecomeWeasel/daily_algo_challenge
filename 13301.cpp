#include <iostream>

using namespace std;

int n;

long long dp[81];


long long ans();

int main(void){
  cin>>n;
  cout << ans();
}

long long ans(){
  dp[1]=1;
  dp[2]=1;
  for(int i=3;i<=n;i++){
    dp[i]=dp[i-1]+dp[i-2];
  }

  return dp[n]*2+(dp[n-1]+dp[n])*2;
}