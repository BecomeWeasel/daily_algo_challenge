#include <iostream>
#include <queue>
#include <vector>

using namespace std;

priority_queue<long long, vector<long long>, greater<long long>> card_pq;

int n, m;

long long ans();

int main(void) {
  cin >> n >> m;

  for (int i = 0; i < n; i++) {
    int tmp;
    cin >> tmp;
    card_pq.push(tmp);
  }
  cout << ans();
}

long long ans() {
  long long card_sum = 0;

  for (int i = 0; i < m; i++) {
    long long first = card_pq.top();
    card_pq.pop();

    long long second = card_pq.top();
    card_pq.pop();

    card_pq.push(first + second);
    card_pq.push(first + second);
  }

  for (int i = 0; i < n; i++) {
    card_sum += card_pq.top();
    card_pq.pop();
  }
  return card_sum;
}