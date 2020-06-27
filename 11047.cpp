#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define MAX 10

int N, K, coin_count;
vector<int> coin(MAX, 0);

int ans();

int main(void) {
  coin_count = 0;
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    cin >> coin[i];
  }
  cout << ans();
}

int ans() {
  for (int i = N - 1; i >= 0 && K > 0; i--) {
    while (K>=coin[i]) {
      K -= coin[i];
      coin_count++;
    }
  }

  return coin_count;
}
