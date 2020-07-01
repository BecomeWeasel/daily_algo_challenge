#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

#define MAX 9

int K;
vector<char> operator_set(9);
vector<bool> c(MAX + 1, false);
vector<string> result_set;

void ans();

void dfs(int, int, string);

bool possible(int, int, char);

int main(void) {
  cin >> K;
  for (int i = 0; i < K; i++) {
    cin >> operator_set[i];
  }

  ans();
}

void ans() {
  string s("");
  for (int i = 0; i < 10; i++) {
    c[i] = true;
    dfs(i, 1, s + to_string(i));
    c[i] = false;
  }

  // 처음 dfs 호출과
  // 재귀 dfs 호출 모두 순서대로 진행하니
  // 가장 앞에 결과가 가장 작은것이고 맨 끝에것이 가장 큰것
  cout << result_set[result_set.size() - 1] << endl << result_set[0];
}

void dfs(int num, int size, string s) {
  if (size == K + 1) {
    result_set.push_back(s);
    return;
  }
  for (int i = 0; i <= 9; i++) {
    if (!c[i] && possible(num, i, operator_set[size - 1])) {
      c[i] = true;
      dfs(i, size + 1, s + to_string(i));
      c[i] = false;
    }
  }
}

bool possible(int a, int b, char op) {
  if (op == '>') return a > b;
  if (op == '<') return a < b;

  // non-reachable
  return true;
}