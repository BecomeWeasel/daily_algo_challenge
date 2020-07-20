#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 21

int N;
int L[N_MAX];
int J[N_MAX];

int ans();

int main(void) {
  cin >> N;

  for (int i = 1; i <= N; i++) {
    cin >> L[i];
  }
  for (int i = 1; i <= N; i++) {
    cin >> J[i];
  }
  cout << ans();
}

int ans() {
  int dp[N_MAX][101] = {0};

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <=100; j++) {

      // 현재 체력이 j이고 i번째 쓰는 체력이
      // j보다 많으면 인사할수 없음
      // i-1번째 사람과 인사했을때 기쁨과 같음
      if (L[i] > j) {
        dp[i][j] = dp[i - 1][j];
      }
      // 현재 체력이 j이고 i번째 쓰는 체력이
      // j랑 작거나 같으면 인사를 할 수 있음
      // i-1번째 사람과 체력이 j-L[i]일때의 기쁨에서
      // L[i]만큼의 체력을 사용하고 기쁨은 J[i]가 추가됨
      // 이것과 이전에 i-1번째 사람까지만의 최대 기쁨과 비교
      else{
        dp[i][j]=max(dp[i-1][j-L[i]]+J[i],dp[i-1][j]);
      }
    }
  }


  // 100이 아니고 99인 이유는
  // 100이면 체력이 0이므로 세준이가 죽은것임
  // 99일때 가장 체력을 다쓴상태이므로 
  return dp[N][99];
}