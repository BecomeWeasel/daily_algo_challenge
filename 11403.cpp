#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define MAX 100

int num;
vector<vector<int>> vector_2d(MAX, vector<int>(MAX, 0));
vector<vector<bool>> is_visited(MAX, vector<bool>(MAX, false));
vector<vector<int>> result(MAX, vector<int>(MAX, 0));

void ans();

void dfs(int, int, int);

int main(void) {
  cin >> num;
  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      int tmp;
      cin >> tmp;
      vector_2d[i][j] = tmp;
    }
  }
  ans();
}

void ans() {
  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      if (!is_visited[i][j] && vector_2d[i][j]) {
        dfs(i, i, j);
      }
    }
  }

  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      cout << result[i][j] << " ";
    }
    cout << '\n';
  }
}

void dfs(int top, int src, int dest) {
  result[top][dest] = 1;
  is_visited[top][dest] = true;
  for (int i = 0; i < num; i++) {
    if (!is_visited[top][i] && vector_2d[dest][i]) {
      dfs(top, dest, i);
    }
  }
}
