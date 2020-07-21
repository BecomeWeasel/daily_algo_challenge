#include <iostream>
#include <numeric>
#include <queue>
#include <vector>

using namespace std;

#define N_MAX 41

vector<int> vip;
vector<int> cases;

int dp[N_MAX];
int N, M;

void fill_dp();

int ans();

int main(void) {
  cin >> N >> M;
  fill_dp();
  vip.push_back(0);
  for (int i = 0; i < M; i++) {
    int tmp;
    cin >> tmp;
    vip.push_back(tmp);
  }
  cout << ans();
}

int ans() {
  int i = 1;
  while (i <= M) {

    /* 첫번째 vip자리까지 일반인이 몇명있는지
    하지만 이방식은 vip가 0명일때 vip[0]에 대해서
    잘못된 접근을 해서 RE
    cases.push_back(dp[vip[0] - 1]);
    
    */

    // i+1번째 vip와 i번째 vip 사이 몇명 있는지
    // n명 있다면 경우의 수는 dp[n]
    cases.push_back(dp[vip[i] - vip[i - 1] - 1]);
    i++;
  }
  //마지막 vip부터 끝까지 일반인이 몇명 있는지
  cases.push_back(dp[N - vip[M]]);

  int total_case = 1;

  // 모든 경우의 수는
  // vip 좌석간의 사람수들이 앉는 경우의 수들을
  // 모두 곱한것
  for (const auto& e : cases) {
    total_case *= e;
  }
  return total_case;
}

void fill_dp() {
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2;
  for (int i = 3; i <= N; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
}