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

void dfs(int, int);

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
    dfs(i, i);
  }


  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      cout << result[i][j] << " ";
    }
    cout << '\n';
  }
}

void dfs(int src, int dest) {
  for (int j = 0; j < num; j++) {
    if (vector_2d[dest][j] && !result[src][j]) {
      result[src][j]=1;
      dfs(src, j);
    }
  }
}
