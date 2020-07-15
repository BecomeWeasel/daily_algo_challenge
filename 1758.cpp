#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define NAMX 100001

int N;
priority_queue<int> pq;

long long ans();

int main(void) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    int tmp;
    cin >> tmp;
    pq.push(tmp);
  }

  cout << ans();
}

long long ans() {
  long long tips = 0;
  for (int i = 1; i <= N; i++) {
    pq.top() - (i - 1) > 0 ? tips += pq.top() - (i - 1) : 0;
    pq.pop();
  }
  return tips;
}