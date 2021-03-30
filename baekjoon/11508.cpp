#include <iostream>
#include <queue>

using namespace std;

priority_queue<int> costs;

int N;

int ans();

int main(void) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    int tmp;
    cin >> tmp;
    costs.push(tmp);
  }
  cout << ans();
}

int ans() {
  // 세번째 구매가 최대한 큰 금액이여함
  // 그래야 총 금액이 최대한 절약됨

  int total_cost = 0;

  int set = 0;
  while (!costs.empty()) {
    // set : 몇번째 구매인지
    set = (set + 1) % 3;

    // 한 꾸러미에서 세번째구매는 
    // 무료임
    if (set != 0) {
      total_cost += costs.top();
    }

    costs.pop();
  }
  return total_cost;
}