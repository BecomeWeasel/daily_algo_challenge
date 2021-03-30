#include <iostream>
#include <vector>

using namespace std;

#define NMAX 11

int N, S, R;
vector<int> kayak(NMAX, 1);

int ans();

int main(void) {
  cin >> N >> S >> R;
  for (int i = 0; i < S; i++) {
    int problem;
    cin >> problem;

    kayak[problem] -= 1;
  }

  for (int i = 0; i < R; i++) {
    int reserve;
    cin >> reserve;

    kayak[reserve] += 1;
  }
  cout << ans();
}

int ans() {
  int cnt = 0;

  if (kayak[1] == 0) {
    if (kayak[2] == 2) {
      // 1번이 카약이 없고 2번이 여유 카약이 있으면
      // 2번이 1번에게 빌려줌
      kayak[1] = kayak[2] = 1;
    } else {
      // 1번이 카약이 없고 2번이 여유 카약이 없으면
      // 1번은 출전 불가
      cnt++;
    }
  }
  for (int i = 2; i < N; i++) {
    // i번이 카약이 없으면
    if (kayak[i] == 0) {
      
      // i-1번이 여유 카약이 있으면 빌려줌
      if (kayak[i - 1] == 2) {
        kayak[i - 1] = 1;
        kayak[i] = 1;
      }
      // i-1은 여유가 없지만 i+1번이 여유 카약이 있으면 빌려줌 
      else if (kayak[i + 1] == 2) {
        kayak[i + 1] = 1;
        kayak[i] = 1;
      } else
        cnt++;
    }
  }
  if (kayak[N] == 0) {
    if (kayak[N-1] == 2) {
      // N번이 카약이 없고 N-1번이 여유 카약이 있으면
      // N-1번이 N번에게 빌려줌
      kayak[N] = kayak[N-1] = 1;
    } else {
      // N번이 카약이 없고 N번이 여유 카약이 없으면
      // N번은 출전 불가
      cnt++;
    }
  }
  return cnt;
}