#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define MAX 25

int total_complex;
int square_size;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));
vector<vector<int>> map(MAX, vector<int>(MAX, 0));
vector<int> s;

void ans();

void dfs(int, int, int*);

int main(void) {
  total_complex = 0;

  cin >> square_size;
  for (int i = 0; i < square_size; i++) {
    string tmp;
    cin >> tmp;
    for (int j = 0; j < square_size; j++) {
      map[i][j] = tmp[j] - '0';
    }
  }
  ans();
}

void ans() {
  for (int i = 0; i < square_size; i++) {
    for (int j = 0; j < square_size; j++) {
      if (!visited[i][j] && map[i][j] == 1) {
        total_complex++;
        visited[i][j] = true;
        int size = 1;
        dfs(j, i, &size);
        s.push_back(size);
      }
    }
  }
  sort(s.begin(), s.end());
  cout << total_complex << '\n';
  for (int i : s) {
    cout << i << '\n';
  }
}

void dfs(int x, int y, int* size_ptr) {
  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if(nx>=square_size||nx<0||ny<0||ny>=square_size) continue;
    if (map[ny][nx] == 1 && !visited[ny][nx]) {
      (*size_ptr)++;
      visited[ny][nx] = true;
      dfs(nx, ny, size_ptr);
    }
  }
}