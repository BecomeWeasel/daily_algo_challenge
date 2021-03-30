#include <iostream>
#include <vector>
using namespace std;

#define MAP_SIZE_MAX 50
#define CABBAGE_MAX 50
#define OP_NUM 4

vector<vector<bool>> map(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));
vector<vector<bool>> visited(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));

int worm_num, M, N, K;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

void dfs(int, int);

int ans();

int main(void) {
  int test_num;
  cin >> test_num;
  while (test_num--) {
    cin >> M >> N >> K;

    for (int i = 0; i < K; i++) {
      int x, y;
      cin >> x >> y;
      map[y][x] = true;
    }

    cout << ans() << '\n';
  }
}
int ans() {
  worm_num = 0;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (map[i][j] && !visited[i][j]) {
        // 지렁이가 있고 방문하지 않은 땅에 대해서
        worm_num++;
        visited[i][j] = true;
        dfs(j, i);
      }
    }
  }

  // 다음 테스트 케이스를 위해서 다시 되돌림
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      map[i][j] = false;
      visited[i][j] = false;
    }
  }

  return worm_num;
}

void dfs(int x, int y) {
  for (int i = 0; i < OP_NUM; i++) {
    int nx = dx[i] + x;
    int ny = dy[i] + y;
    if (nx >= M || ny >= N || nx < 0 || ny < 0) {
      continue;
    }
    if (map[ny][nx] && !visited[ny][nx]) {
      visited[ny][nx] = true;
      dfs(nx, ny);
    }
  }
}