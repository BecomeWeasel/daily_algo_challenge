#include <iostream>

using namespace std;

#define NMAX 101

int scores[NMAX];

int N;

int ans();

int main(void) {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    cin >> scores[i];
  }
  cout << ans();
}

int ans() {
  int cnt=0;
  for (int i = N - 1; i > 0; i--) {
    while (scores[i] >= scores[i + 1]) {
      scores[i] -= 1;
      cnt++;
    }
  }
  return cnt;
}