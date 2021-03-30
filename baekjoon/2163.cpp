#include <iostream>
#include <vector>

using namespace std;

#define MAX 300

int dp[MAX+1][MAX+1];

int N,M;

int ans();

int main(void){
  cin>>N>>M;
  cout<<ans();
}

int ans(){
  dp[1][1]=0;
  dp[2][1]=1;
  for(int i=2;i<=N;i++){
    dp[i][1]=dp[i-1][1]+1;
  }
  for(int i=1;i<=N;i++){
    for(int j=1;j<=M;j++){
      dp[i][j]=dp[i][1]*j+j-1;
    }
  }
  return dp[N][M];
}
