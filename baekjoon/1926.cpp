#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define MAP_SIZE_MAX 501

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int n, m, paint_cnt, paint_max;
int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
bool visited[MAP_SIZE_MAX][MAP_SIZE_MAX];

void ans();

int bfs(queue<pair<int, int>>);

int main(void) {
  memset(map, 0, sizeof(map));
  memset(visited, false, sizeof(visited));

  // 그림이 하나도 없을때는 paint_max : 1
  paint_cnt = paint_max = 0;

  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      cin >> map[i][j];
    }
  }
  ans();
}

void ans() {
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      if (map[i][j] == 1 && !visited[i][j]) {
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));
        visited[i][j] = true;
        paint_cnt += 1;

        paint_max = max(paint_max, bfs(q));
      }
    }
  }

  cout << paint_cnt << '\n' << paint_max;
}

int bfs(queue<pair<int, int>> q) {
  int area = 1;
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    for (int k = 0; k < 4; k++) {
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      if (ny > n || nx > m || ny <= 0 || nx <= 0) continue;

      if (map[ny][nx] == 1 && !visited[ny][nx]) {
        q.push(make_pair(ny, nx));
        visited[ny][nx] = true;
        area++;
      }
    }
  }

  return area;
}
