#include <iostream>
#include <vector>

using namespace std;

#define D_MAX 31

int D, K;

int dp_a[D_MAX];
int dp_b[D_MAX];
pair<int, int> partial_sum[D_MAX];

void ans();

int main(void) {
  cin >> D >> K;
  ans();
}

void ans() {
  // dp_a[i] : i번째 떡의 개수에 첫번재 떡의 개수가 몇개 들어가 있는지
  // dp_b[i] : i번째 떡의 개수에 2번째 떡의 개수가 몇개 들어가 있는지
  dp_a[1] = dp_b[2] = 1;
  dp_a[2] = dp_b[1] = 0;

  for (int i = 3; i <= D; i++) {
    dp_a[i] = dp_a[i - 1] + dp_a[i - 2];
    dp_b[i] = dp_b[i - 1] + dp_b[i - 2];
  }

  for (int i = 1; i < K; i++) {
    for (int j = i; j < K; j++) {
      if ((K - dp_a[D] * i) % (dp_b[D] * j) == 0) {
        int tmp = K - dp_a[D] * i;
        if ((tmp - dp_b[D] * j) == 0) {
          cout << i << '\n' << j;
          return;
        } else
          continue;
      }
    }
  }
}