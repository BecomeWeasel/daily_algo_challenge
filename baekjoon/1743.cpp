#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define MAP_SIZE_MAX 101

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
bool visited[MAP_SIZE_MAX][MAP_SIZE_MAX];

int N, M, K, garbage;

int ans();

int bfs(queue<pair<int, int>>);

int main(void) {
  memset(map, 0, sizeof(map));
  memset(visited, false, sizeof(visited));

  cin >> N >> M >> K;
  for (int i = 0; i < K; i++) {
    int x, y;
    cin >> y >> x;
    map[y][x] = 1;
  }
  cout << ans();
}

int ans() {
  garbage = 0;

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      // 방문하지 않은 쓰레기더미일때
      if (map[i][j] == 1 && !visited[i][j]) {
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));
        visited[i][j] = true;

        // (j,i) 좌표에서 발견한 쓰레기더미의 크기를 저장
        int result = bfs(q);

        // 탐색한 쓰레기더미의 크기를 
        // 기존 쓰레기더미의 크기와 비교해 최댓값을 저장
        garbage = max(garbage, result);
      }
    }
  }

  return garbage;
}

int bfs(queue<pair<int, int>> q) {
  int cnt = 0;
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();
    // 쓰레기 더미 크기 늘리기
    cnt++;

    for (int k = 0; k < 4; k++) {
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      if (ny > N || nx > M || nx <= 0 || ny <= 0) continue;

      // 기존의 쓰레기와 인접해있고 방문하지 않았을때
      if (map[ny][nx] == 1 && !visited[ny][nx]) {
        visited[ny][nx]=true;
        q.push(make_pair(ny,nx));
      }
    }
  }

  return cnt;
}