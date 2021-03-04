#include <iostream>

using namespace std;

#define NMAX 100001

int dp[NMAX];
int N;
int ans();

int main(void){
  cin>>N;
  cout<<ans();
}

int ans(){
  fill(dp,dp+NMAX,987654321);
  dp[0]=0;
  dp[1]=dp[2]=dp[5]=dp[7]=1;
  dp[3]=dp[4]=dp[6]=2;

  // i원을 낼때
  // i-1원을 낼때처럼 내고 1원 1개 더내고
  // 1-2원을 낼때처럼 내고 2원 1개 더내고
  // i-5원을 낼때처럼 내고 5원 1개 더내고
  // i-7원을 낼때처럼 내고 7원 1개 더내고
  // 이 방법중 가장 적게 내는 방법을 고른후 1개만 더내면됨
  for(int i=8;i<=N;i++){
    dp[i]=min(min(min(dp[i-1],dp[i-2]),dp[i-5]),dp[i-7])+1;
  }

  return dp[N];
} 