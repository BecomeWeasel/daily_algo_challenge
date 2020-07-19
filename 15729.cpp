#include <iostream>
#include <vector>

using namespace std;

#define NMAX 1000000

int target[NMAX];
int light[NMAX] = {0};
int N;

void light_on(int);

int ans();

int main(void) {
  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> target[i];
  }

  cout << ans();
}

int ans() {
  int cnt = 0;

  for (int i = 0; i < N; i++) {
    if (target[i] != light[i]){
      light_on(i);
      cnt++;
    }
  }

  return cnt;

}

void light_on(int press_idx) {
  for (int i = press_idx; i < N, i < press_idx + 3; i++) {
    // 0일 경우에 1로 , 1인 경우에 0으로
    light[i] = light[i] == 0 ? 1 : 0;
  }
}