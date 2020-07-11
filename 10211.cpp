#include <iostream>
#include <vector>

using namespace std;

#define NMAX 1001

int N;

int ans(vector<int>);

int main(void) {
  int test_num;

  cin >> test_num;
  while (test_num--) {
    /* code */
    cin >> N;
    vector<int> v;
    v.push_back(0);
    for (int i = 0; i < N; i++) {
      int tmp;
      cin >> tmp;
      v.push_back(tmp); 
    }

    cout << ans(v) << '\n';
  }
}

int ans(vector<int> v) { 
  int dp[NMAX];
  int max_result;
  dp[1]=max_result=v[1];

  for(int i=2;i<=N;i++){
    dp[i]=max(dp[i-1]+v[i],v[i]);
    max_result=max(max_result,dp[i]);
  }
  return max_result;
 }
