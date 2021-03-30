#include <string.h>

#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 51

int W, H, MAX_DIST;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

vector<vector<bool>> map(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));
vector<vector<bool>> check(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));

void bfs(queue<pair<int, int>>);

int ans();

int main(void) {
  cin >> H >> W;
  for (int i = 1; i <= H; i++) {
    string s;
    cin >> s;
    for (int j = 1; j <= W; j++) {
      if (s[j - 1] == 'W')
        map[i][j] = false;
      else
        map[i][j] = true;
    }
  }
  cout << ans();
}

int ans() {
  MAX_DIST = 0;
  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      if (map[i][j]) {
        queue<pair<int, int>> q;
        check[i][j] = true;
        q.push(make_pair(i, j));
        bfs(q);
        // 모든 육지인 점에 대해서 bfs를 수행해야함.
      }

      for (int k = 1; k <= H; k++) {
        fill(check[k].begin(), check[k].end(), false);
      }
      // bfs가 map에서 육지의 개수만큼 호출되므로 
      // check 전역변수는 계속 초기화
    }
  }

  return MAX_DIST;
}

void bfs(queue<pair<int, int>> q) {
  // bfs를 처음 호출한 육지에서부터의 거리
  int dist[MAP_SIZE_MAX][MAP_SIZE_MAX];
  // 바다 건너의 섬이나 바다는 dist를 0이 유지됨
  memset(dist, 0, sizeof(dist[0][0]) * MAP_SIZE_MAX * MAP_SIZE_MAX);
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();
    for (int i = 0; i < 4; i++) {
      // 중앙을 기준으로 4방향 순회
      int ny = front.first + dy[i];
      int nx = front.second + dx[i];

      // ny와 nx가 map을 벗어나지 않게함 없으면 RE로 실패
      if (nx > W || ny > H || ny < 1 || nx < 1) continue;

      if (map[ny][nx] && !check[ny][nx]) {
        check[ny][nx] = true;
        dist[ny][nx] = dist[front.first][front.second] + 1;
        q.push(make_pair(ny, nx));
      }
    }
  }

  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      MAX_DIST = max(dist[i][j], MAX_DIST);
      // 한 섬의 육지를 기준으로 bfs를 계속 호출하니
      // src에서 가장 먼점까지의 최대거리가 계속 갱신되어야함 
    }
  }
}