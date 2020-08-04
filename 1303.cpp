#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define MAP_SIZE_MAX 101

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
bool visited[MAP_SIZE_MAX][MAP_SIZE_MAX];
int N, M, white, blue;

void ans();

int bfs(queue<pair<int, int>>);

int main(void) {
  memset(map, 0, sizeof(map));
  memset(visited, false, sizeof(visited));
  white = blue = 0;

  cin >> N >> M;
  for (int i = 1; i <= M; i++) {
    string s;
    cin >> s;
    for (int j = 1; j <= N; j++) {
      switch (s[j - 1]) {
        case 'W':
          map[i][j] = 0;
          break;

        case 'B':
          map[i][j] = 1;
          break;
      }
    }
  }
  ans();
}

void ans() {
  for (int i = 1; i <= M; i++) {
    for (int j = 1; j <= N; j++) {
      if (!visited[i][j]) {
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));
        visited[i][j] = true;

        int result = bfs(q);
        if (map[i][j] == 0) {
          white += result * result;
        } else {
          blue += result * result;
        }
      }
    }
  }

  cout << white << " " << blue;
}

int bfs(queue<pair<int, int>> q) {
  int cnt = 0;
  int color = 0;
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();
    cnt++;

    // 처음 시도에만 색구별하는데 사용됨
    color = map[front.first][front.second];

    for (int k = 0; k < 4; k++) {
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      // map을 벗어낫다면
      if (ny > M || nx > N || ny <= 0 || nx <= 0) continue;

      // 현재 색과 새로 방문할 색이 같고
      // 방문한적 없으면
      // 탐색 추가
      if (!visited[ny][nx] && map[ny][nx] == color) {
        q.push(make_pair(ny, nx));
        visited[ny][nx] = true;
      }
    }
  }
  return cnt;
}