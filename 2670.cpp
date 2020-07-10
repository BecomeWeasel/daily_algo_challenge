#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

#define NMAX 10001

double dp[NMAX];
double numbers[NMAX];

int n;
double max_result;

void ans();

int main(void){
  cin>>n;
  for(int i=1;i<=n;i++){
    cin>>numbers[i];
  }
  ans();
}

void ans(){
  max_result=dp[1]=numbers[1];

  for(int i=2;i<=n;i++){
    dp[i]=max(dp[i-1]*numbers[i],numbers[i]);
    max_result=max(max_result,dp[i]);
  }
  cout<<fixed;
  cout.precision(3);
  cout<<max_result;
}