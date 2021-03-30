#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define NMAX 1001

int J, N;

int ans(priority_queue<int>);

int main(void) {
  int test_num;
  cin >> test_num;
  while (test_num--) {
    priority_queue<int> pq;
    cin >> J >> N;
    for (int i = 0; i < N; i++) {
      int r, c;
      cin >> r >> c;
      // 상자에 사탕은 r*c만큼 넣을수 있음
      // 그리디하게 풀어야 하니 pq에 상자에 넣을수 있는
      // 사탕의 개수만큼 넣음
      pq.push(r * c);
    }
    cout << ans(pq) << '\n';
  }
}

int ans(priority_queue<int> pq) {
  int cnt = 0;
  while (J > 0) {
    int front = pq.top();
    pq.pop();
    J -= front;
    cnt++;
  }
  return cnt;
}
