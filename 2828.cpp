#include <iostream>
#include <vector>

using namespace std;

#define APPLE_MAX 21

int N, M, J, left_end, right_end;
int apple[APPLE_MAX];

int ans();

int main(void) {
  cin >> N >> M >> J;
  for (int i = 1; i <= J; i++) {
    cin >> apple[i];
  }
  cout << ans();
}

int ans() {
  int dist = 0;
  left_end = 1;
  right_end = left_end + M - 1;
  for (int i = 1; i <= J; i++) {
    if (apple[i] > right_end) {
      // 사과가 바구니 오른쪽끝보다 멀리있다면
      // apple[i]-rear만큼 바구니가 오른쪽으로 이동해야함
      int move = apple[i] - right_end;
      right_end += move;
      left_end += move;

      dist += move;

    } else if (apple[i] < left_end) {
      // 사과가 바구니 왼쪽끝보다 멀리있다면
      // left_end-apple[i]만큼 바구니가 왼쪽으로 이동해야함
      int move = left_end - apple[i];
      right_end -= move;
      left_end -= move;

      dist += move;
    } 
  }
  return dist;
}
