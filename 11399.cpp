#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <numeric>
using namespace std;

#define MAX 1001

int N;
vector<int> p(MAX, 0);
vector<int> t(MAX, 0);
priority_queue<int, vector<int>, greater<int>> pq;

int ans();

int main(void) {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    int tmp;
    cin >> tmp;
    pq.push(tmp);
  }
  cout << ans();
}

int ans() {
  for (int i = 1; i <= N; i++) {
    t[i] = pq.top() + t[i - 1];
    pq.pop();
  }

  int sum=accumulate(t.begin(),t.end(),0);
  
  return sum;
}