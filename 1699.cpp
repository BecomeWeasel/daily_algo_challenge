#include <math.h>

#include <iostream>

using namespace std;

#define NMAX 100001

int dp[NMAX];

int N;

int ans();

bool IsSquare(unsigned int num) {
  unsigned int temp = (unsigned int)(sqrt((double)num) + 0.5);
  return temp * temp == num;
}

int main(void) {
  cin >> N;
  cout << ans();
}

int ans() {
  fill(dp, dp + NMAX, 987654321);

  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 3;

  for (int i = 4; i <= N; i++) {

    // i가 k의 제곱수라면
    // i=k^2로 나타낼수 있음.
    // 9=3^2
    // 10=9+1=3^2+1^2
    // 13=9+4=3^2+2^2
    if (IsSquare(i)) {
      dp[i] = 1;
      continue;
    }
    for (int j = 1; j*j <= i; j++) {
      dp[i] = min(dp[i], dp[i-j*j]+1);
    }
  }

  return dp[N];
}