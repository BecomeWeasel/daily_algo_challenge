#include <iostream>
#include <vector>

using namespace std;

#define T_MAX 1001
#define W_MAX 31

// dp[i][w][1]= i번째에 1번에 있을때 w만큼 움직였을때 먹을수잇는 자두

int plum[T_MAX];

int T, W;

int ans();

int main(void) {
  cin >> T >> W;

  for (int i = 1; i <= T; i++) {
    cin >> plum[i];
  }
  cout << ans();
}

int ans() {
  int dp[T_MAX][W_MAX][3]={0};

  //초기값 설정
  dp[1][0][1] = plum[1] == 1 ? 1 : 0;
  dp[1][1][2] = plum[1] == 2 ? 1 : 0;

  for (int i = 2; i <= T; i++) {
    for (int j = 0; j <= W; j++) {
      if (j > 0) {
        // 자두가 1번에 떨어질때
        if (plum[i] == 1) {
          // i-1번째일때 2번에서 이동해서 먹거나
          // i-1번째일때 1번에서 그대로 있어서 먹거나
          dp[i][j][1] = max(dp[i - 1][j - 1][2], dp[i - 1][j][1]) + 1;

          // i-1번째일때 2번에서 그대로 있어서 못먹거나
          // i-1번째일때 1번에서 옮겨서 못먹거나
          dp[i][j][2] = max(dp[i - 1][j][2], dp[i - 1][j - 1][1]);
        } else {
          // i-1번째일때 2번에서 그대로 있어서 한개먹거나
          // i-1번째일때 1번에서 움직여서 한개 먹거나
          dp[i][j][2] = max(dp[i - 1][j][2], dp[i - 1][j - 1][1]) + 1;

          // i-1번째일때 1번에서 그대로 있어서 못 먹거나
          // i-1번째일때 2번에서 옮겨서 못먹거나
          dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][2]);
        }
      } else {
          
        // 계속 안움직일때 (j가 0보다 작아지는것 방지)
        if (plum[i] == 1) {
          // 1일때 안움직이면
          dp[i][0][1]=dp[i-1][0][1]+1;
          dp[i][0][2]=dp[i-1][0][2];
        } else {
          //2일때 안움직이면
          dp[i][0][1]=dp[i-1][0][1];
          dp[i][0][2]=dp[i-1][0][2]+1;
        }
      }
    }
  }

  int max_value = -1;
  for (int i = 0; i <= W; i++) {
    max_value = max(max_value, max(dp[T][i][1], dp[T][i][2]));
  }
  return max_value;
}