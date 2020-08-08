#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define CHAR_MAX 1001

int N, M, src, dest;
bool connected[CHAR_MAX][CHAR_MAX];
bool visited[CHAR_MAX];

int ans();

int bfs(queue<pair<int, int>>);

int main(void) {
  cin >> src >> dest >> N >> M;
  memset(visited, false, sizeof(visited));
  memset(connected, false, sizeof(connected));
  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    connected[a][b] = connected[b][a] = true;
  }

  cout << ans();
}

int ans() {
  queue<pair<int, int>> q;
  q.push({src, 0});
  visited[src] = true;

  return bfs(q);
}

int bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    if (front.first == dest) {
      return front.second;
    }

    for (int i = 1; i <= N; i++) {
      if (!visited[i] && connected[front.first][i]) {
        visited[i] = true;
        q.push({i, front.second + 1});
      }
    }
  }
  return -1;
}
