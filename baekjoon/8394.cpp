#include <iostream>

using namespace std;

#define N_MAX 10000001

int dp[N_MAX];

int n;

int ans();

int main(void){
  cin>>n;
  cout<<ans();

}

int ans(){
  dp[1]=1;
  dp[2]=2;
  dp[3]=3;
  for(int i=4;i<=n;i++){
    dp[i]=((dp[i-2]%10)+(dp[i-1]%10))%10;
  }

  return dp[n];
}