#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

void ans(int, int);

void dfs(int, int, vector<bool>, stack<int>);

bool isPromising(int, vector<bool>);

void print(stack<int>);  // 체크 다풀고

int main(void) {
  int range, length;
  cin >> range >> length;
  ans(range, length);
}

void ans(int range, int length) {
  // stack<int> s;
  // s.push(0);
  for (int i = 1; i < range + 1; i++) {
    stack<int> s;
    // s.push(0);
    vector<bool> check(range + 1);
    fill(check.begin(), check.end(), false);
    check[0] = true;
    dfs(i, length, check, s);
  }
}

void dfs(int num, int len, vector<bool> check, stack<int> s) {
  if (isPromising(num, check)) {
    s.push(num);
    check[num] = true;
    // cout <<"check size is " <<check.size()<<endl;
    for (int i = 1; i < check.size(); i++) {
      dfs(i, len, check, s);
    }
    if (s.size() == len) {
      print(s);
    }
    s.pop();
  } else
    return;
}

bool isPromising(int num, vector<bool> check) {
  if (check[num])
    return false;
  else
    return true;
}

void print(stack<int> s) {
  // cout<<"stack size : "<<s.size()<<endl;
  // stack을 거꾸로 출력
  stack<int>r_s;
  int size = s.size();
  for (int i = 0; i < size; i++) {
    // cout << "current push back is " << s.top() <<" c I "<<i<< endl;
    r_s.push(s.top());
    s.pop();
  }
  // cout << "vector size : " << tmp.size() << endl;

  for (int i = 0; i < size; i++) {
    cout << r_s.top() << " ";
    r_s.pop();
  }
  cout<<'\n';
  return;
}