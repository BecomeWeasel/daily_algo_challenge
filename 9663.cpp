#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int ans(int);

bool isPromising(int);

void dfs(int, int);

int cnt = 0;

vector<int> cols(15);

int main(void) {
  int size;
  cin >> size;
  cout << ans(size);
}

int ans(int size) {
  dfs(0, size);
  return cnt;
}

void dfs(int num, int size) {
  if (num == size) {
    cnt++;
  } else {
    for (int i = 0; i < size; i++) {
      cols[num] = i;
      if (isPromising(num)) {
        dfs(num + 1, size);
      }
    }
  }
}

bool isPromising(int num) {
  for (int i = 0; i < num; i++) {
    if (cols[i] == cols[num] || abs(cols[i] - cols[num]) == (num - i))
      return false;
  }
  return true;
}
