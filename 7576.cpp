#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 1000

int days, N, M;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {
    -1,
    1,
    0,
    0,
};

vector<vector<int>> map(MAX, vector<int>(MAX, 0));
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));

int ans();

void bfs(queue<pair<int, int>>);

int main(void) {
  days = 0;
  cin >> M >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      int tmp;
      cin >> tmp;
      map[i][j] = tmp;
    }
  }
  cout << ans();
}

int ans() {
  queue<pair<int, int>> q;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++)
      if (map[i][j] == 1) {
        q.push(make_pair(i, j));
      }
  }

  bfs(q);
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (map[i][j] == 0) return -1;
    }
  }
  return days;
}

void bfs(queue<pair<int, int>> q) {
  queue<pair<int, int>> tmp_q;
  while (true) {
    while (!q.empty()) {
      pair<int, int> front = q.front();
      q.pop();
      for (int i = 0; i < 4; i++) {
        int nx = front.second + dx[i];
        int ny = front.first + dy[i];

        if (nx >= M || ny >= N || nx < 0 || ny < 0) continue;

        if (map[ny][nx] == 0 && !visited[ny][nx]) {
          map[ny][nx] = 1;
          tmp_q.push(make_pair(ny, nx));
        }
      }
      visited[front.first][front.second] = true;
    }

    if (tmp_q.empty())
      return;
    else {
      days++;
      int size = tmp_q.size();
      for (int i = 0; i < size; i++) {
        q.push(tmp_q.front());
        tmp_q.pop();
      }
    }
  }
}