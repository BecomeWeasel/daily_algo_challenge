#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

void ans(int, int);

void dfs(int, int, int, stack<int>, bool);

bool isPromising(int, int, int);

void print(stack<int>);

int main(void) {
  int n, m;
  cin >> n >> m;
  ans(n, m);
}

void ans(int range, int len) {  
  stack<int> s;

  dfs(1, len, range, s, true);  // 1을 선택한 경우

  dfs(1, len, range, s, false);  // 1을 선택하지 않았을경우
}

void dfs(int num, int len, int range, stack<int> s, bool select) {
  if (select) s.push(num);
  if (num > range)
    return;
  else if (isPromising(num, (int)s.size(), len)) {
    dfs(num + 1, len, range, s, true);  // num+1을 선택한 경우

    dfs(num + 1, len, range, s, false);  // num을 선택하지 않았을 경우

  } else if(s.size()==len){
    print(s);
  }
}

bool isPromising(int num, int s_size, int len) {
  if (s_size >= len)
    return false;
  else
    return true;
}

void print(stack<int> s) {
  stack<int> r_s;
  int size = s.size();
  for (int i = 0; i < size; i++) {
    r_s.push(s.top());
    s.pop();
  }

  for (int i = 0; i < size; i++) {
    cout << r_s.top() << " ";
    r_s.pop();
  }
  cout << '\n';
  return;
}