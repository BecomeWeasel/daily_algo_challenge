#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define MAP_SIZE_MAX 101

int dx[8] = {0, 0, -1, 1, 1, 1, -1, -1};
int dy[8] = {1, -1, 0, 0, 1, -1, 1, -1};

int n, m;

int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
bool visited[MAP_SIZE_MAX][MAP_SIZE_MAX];

int ans();

void bfs(queue<pair<int, int>>);

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  while (true) {
    cin >> n >> m;
    if (n * m == 0) {
      // return 1 하니 RE
      // return 1;
      return 0;
    }

    for (int i = 1; i <= n; i++) {
      string s;
      cin >> s;
      for (int j = 1; j <= m; j++) {
        // 오일이 아니면 map[i][j]에 0을
        // 오일이면 1을
        map[i][j] = s[j - 1] == '*' ? 0 : 1;
      }
    }

    cout << ans() << '\n';
  }
}

void bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    for (int k = 0; k < 8; k++) {
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      if (ny > n || nx > m || ny < 1 || nx < 1) continue;

      if (!visited[ny][nx] && map[ny][nx] == 1) {
        q.push(make_pair(ny, nx));
        visited[ny][nx] = true;
      }
    }
  }
}

int ans() {
  int oil = 0;

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      if (map[i][j] == 1 && !visited[i][j]) {
        oil++;
        visited[i][j] = true;
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));
        bfs(q);
      }
    }
  }

  memset(visited, false, sizeof(visited));
  memset(map, 0, sizeof(map));

  return oil;
}