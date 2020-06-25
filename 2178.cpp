#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 100
#define DISTANCE_MAX 10000000

vector<vector<int>> map(MAX, vector<int>(MAX, 0));
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));
vector<vector<int>> distance_map(MAX, vector<int>(MAX, DISTANCE_MAX));
int N, M;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

int ans();

void bfs(queue<pair<int, int>>);

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < M; j++) {
      map[i][j] = s[j] - '0';
    }
  }

  cout << ans();
}

int ans() {
  queue<pair<int, int>> q;
  q.push(make_pair(0, 0));

  distance_map[0][0] = 1;
  visited[0][0] = true;

  bfs(q);

  return distance_map[N - 1][M - 1];
}

void bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> tos = q.front();
    q.pop();
    for (int i = 0; i < 4; i++) {
      int nx = tos.first + dx[i];
      int ny = tos.second + dy[i];

      if (nx >= M || ny >= N || nx < 0 || ny < 0) continue;
      if (distance_map[ny][nx] >= distance_map[tos.second][tos.first]) {
        distance_map[ny][nx] = distance_map[tos.second][tos.first] + 1;
      }

      if (map[ny][nx] == 1 && !visited[ny][nx]) {
        visited[ny][nx] = true;
        q.push(make_pair(nx, ny));
      }
    }
  }
}