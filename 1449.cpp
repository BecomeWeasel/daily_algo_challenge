#include <iostream>
#include <vector>

using namespace std;

#define N_MAX_10_TIMES 10006

vector<bool> leak(N_MAX_10_TIMES, false);

int N, L;

int ans();

int main(void) {
  cin >> N >> L;
  for (int i = 0; i < N; i++) {
    int tmp;
    cin >> tmp;

    // 고장난 곳 좌우로 0.5만큼 메꿔야하니
    // 1이 고장나면 5부터 15가 고장났다고 표시
    for (int j = -5; j <= 5; j++) {
      leak[tmp * 10 + j] = true;
    }
  }
  cout << ans();
}

int ans() {
  int cnt = 0;
  int i = 5;
  while (i < N_MAX_10_TIMES) {
    if (leak[i] == true) {
      int used_length = 0;

      // 주어진 길이의 테이프를 다쓸때까지
      // 위치가 10배이니 테이프길이도 10배로
      while (used_length <= L * 10) {
        used_length++;
        i++;
      }
      cnt++;
    } else {
      i++;
    }
  }
  return cnt;
}