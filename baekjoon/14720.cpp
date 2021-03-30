#include <iostream>
#include <vector>

using namespace std;

#define NMAX 1000

int store[NMAX];

int N;

int ans();

int main(void) {
  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> store[i];
  }

  cout << ans();
}

int ans() {
  int cnt = 0;
  int state = 0;

  for (int i = 0; i < N; i++) {
    if (store[i] == state) {
      cnt++;
      state=(state+1)%3;
    }
  }

  return cnt;
}