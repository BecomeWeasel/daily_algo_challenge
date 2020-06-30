#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define N_MAX 100
#define M_MAX 50

int N, M, money, six, single;

int ans();

int main(void) {
  money = 0;
  six = 1000000;
  single = 100000;
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int tmpa, tmpb;
    cin >> tmpa >> tmpb;
    if (six > tmpa) {
      six = tmpa;
    }
    if (single > tmpb) {
      single = tmpb;
    }
  }
  cout << ans();
}

int ans() {
  if (six > single * 6) {
    return single * N;
  }
  while (N > 0) {
    if (N >= 6) {
      money += six;
      N -= 6;
    } else {
      money += min(six, single * N);
      N = 0;
    }
  }
  return money;
}