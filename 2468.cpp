#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 101

vector<vector<int>> map(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, -1));
vector<vector<bool>> flood(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));
vector<vector<bool>> check(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));
int N, max_height, max_count;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int ans();

void bfs(queue<pair<int, int>>);

int main(void) {
  cin >> N;
  max_height = -1;
  max_count = -1;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> map[i][j];
      max_height = max(max_height, map[i][j]);
    }
  }
  cout << ans();
}

int ans() {
  for (int height = max_height; height >= 0; height--) {
    int candidate_max_count = 0;

    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        // 물의 높이보다 낮은곳은 잠기게
        flood[i][j] = map[i][j] <= height;
        check[i][j] = false;
      }
    }

    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        // 안 잠긴곳이 있다면 거기서부터 bfs 탐색
        if (!flood[i][j] && !check[i][j]) {
          queue<pair<int, int>> q;
          q.push(make_pair(i, j));
          check[i][j] = true;
          candidate_max_count++;
          bfs(q);
        }
      }
    }
    max_count = max(max_count, candidate_max_count);
  }
  return max_count;
}

void bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();
    for (int i = 0; i < 4; i++) {
      // 물에 안잠긴곳을 기준으로 상하좌우 탐색
      int nx = front.second + dx[i];
      int ny = front.first + dy[i];
      if (nx > N || ny > N || ny < 1 || nx < 1) continue;

      // 물에 아직 안잠기고 방문하지 않았다면 
      // 큐에 넣어줌
      if (!flood[ny][nx] && !check[ny][nx]) {
        q.push(make_pair(ny, nx));
        check[ny][nx] = true;
      }
    }
  }
}