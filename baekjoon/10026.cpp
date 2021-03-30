#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MAX 100

vector<vector<int>> map(MAX, vector<int>(MAX, -1));
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));
// vector<vector<bool>> visited_problem(MAX, vector<bool>(MAX, false));

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int num;
int area_count = 0;

void ans();

void dfs(int, int, int);

int main(void) {
  cin >> num;
  for (int i = 0; i < num; i++) {
    string str;
    cin >> str;
    for (int j = 0; j < num; j++) {
      switch (str[j]) {
        case 'R':
          map[i][j] = 0;
          break;
        case 'G':
          map[i][j] = 1;
          break;
        case 'B':
          map[i][j] = 2;
          break;
        case '\n':
          continue;
          break;
      }
    }
  }
  // for (int i = 0; i < num; i++) {
  //   for (int j = 0; j < num; j++) {
  //     cout << map[i][j] << " ";
  //   }
  //   cout << endl;
  // }

  // cout << endl;
  // cout << endl;
  // cout << endl;
  // cout << endl;

  ans();
}

void ans() {
  //정상 기준으로 탐색
  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      if (!visited[i][j]) {
        dfs(map[i][j], j, i);
        area_count++;
      }
    }
  }
  cout << area_count << " ";
  area_count = 0;

  // 색약기준으로 탐색

  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      visited[i][j] = false;
      if (map[i][j] == 1) map[i][j] = 0;
      // 녹색을 모두 빨간색으로 바꿈
    }
  }

  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      if (!visited[i][j]) {
        dfs(map[i][j], j, i);
        area_count++;
      }
    }
  }

  cout << area_count;
}

void dfs(int color, int x, int y) {
  visited[y][x] = true;
  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (nx < 0 || ny < 0 || nx >= num || ny >= num) continue;
    if (map[ny][nx] == map[y][x] && !visited[ny][nx]) {
      dfs(color, nx, ny);
    }
  }
}