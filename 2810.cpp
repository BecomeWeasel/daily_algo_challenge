#include <string.h>

#include <iostream>

using namespace std;

int ans();

string seat;
int N;
int main(void) {
  cin >> N;
  cin >> seat;
  cout << ans();
}

int ans() {
  int cupholder = 1;
  int i = 0;
  while (i < seat.size()) {
    if (seat[i] == 'S') {
      cupholder++;
      i++;
    } else if (seat[i] == 'L') {
      cupholder++;
      i += 2;
    }
  }
  
  // 사람수보다 컵홀더 개수가 많으면
  // N명 모두 놓을수 있음
  return N<cupholder?N:cupholder;
}