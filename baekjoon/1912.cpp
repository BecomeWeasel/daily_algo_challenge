#include <vector>
#include <iostream>

using namespace std;

#define NMAX 100001

int N;
int max_result;
int numbers[NMAX];
int dp[NMAX];

int ans();

int main(void){
  cin >>N;
  for(int i=1;i<=N;i++){
    cin>>numbers[i];
  }
  cout<<ans();
}

int ans(){
  // 입력 값이 모두 음수 일때는 첫번째만 선택하고
  // 아무것도 안더하는게 최댓값
  max_result=dp[1]=numbers[1];
  dp[1]=numbers[1];
  for(int i=2;i<=N;i++){
    // i번째를 선택하고 이전것에 합치거나,
    // 이전것을 버리고 i번째부터 다시 시작해서 선택하거나
    dp[i]=max(dp[i-1]+numbers[i],numbers[i]);
    max_result=max(max_result,dp[i]);
  }



  return max_result;
}