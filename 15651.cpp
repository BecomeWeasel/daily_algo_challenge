#include <iostream>
#include <stack>
#include <vector>

using namespace std;

void ans(int, int);

void dfs(int, int, int, stack<int>);

void print(stack<int>);

int main(void) {
  int n, m;
  cin >> n >> m;
  ans(n, m);
}

void ans(int range, int len) {
  stack<int> s;

  for (int i = 1; i <= range; i++) {
    s.push(i);
    dfs(i, len, range, s);
    s.pop();
  }
}

void dfs(int num, int len, int range, stack<int> s) {
  if (s.size() == len) {
    print(s);
    return;
  }
  for (int i = 1; i <= range; i++) {
    s.push(i);
    dfs(i, len, range, s);
    s.pop();
  }
}

void print(stack<int> s) {
  stack<int> r_s;
  while (s.size() > 0) {
    r_s.push(s.top());
    s.pop();
  }
  while (r_s.size() > 0) {
    cout << r_s.top() << " ";
    r_s.pop();
  }
  cout << '\n';
}