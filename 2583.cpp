#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 101

int M, N, K;
vector<vector<int>> grid(MAX, vector<int>(MAX, 0));
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));
vector<int> size_vector;
priority_queue<int, vector<int>, greater<int>> size_pq;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

void ans();
void dfs(int, int, int*);
int bfs(queue<pair<int, int>>);

int main(void) {
  cin >> M >> N >> K;
  for (int i = 0; i < K; i++) {
    int lx, ly, rx, ry;
    cin >> lx >> ly >> rx >> ry;

    for (int y = ly + 1; y <= ry; y++) {
      for (int x = lx + 1; x <= rx; x++) {
        grid[y][x] = 1;
      }
    }

    /*
    for (int h = lx + 1; h <= rx; h++) {
      for (int j = ly + 1; j <= ry; j++) {
        grid[h][j] = 1;
      }
    }
    */
  }

  /*
  for (int i = M; i >= 1; i--) {
    for (int j = 1; j <= N; j++) {
      cout << grid[i][j] << " ";
    }
    cout << endl;
  }
  */

  ans();
}

void ans() {
  int grid_cnt = 0;
  for (int i = M; i >= 1; i--) {
    for (int j = 1; j <= N; j++) {
      if (grid[i][j] == 0 && !visited[i][j]) {
        visited[i][j] = true;
        /*
        int size = 1;
        dfs(j, i, &size);
        size_vector.push_back(size);
        */

        // 빈 영역을 발견했으니 개수 올림
        grid_cnt++;

        queue<pair<int, int>> q;
        q.push(make_pair(i, j));

        // 발견한 점에 대해서 bfs 탐색
        int result = bfs(q);

        size_pq.push(result);
      }
    }
  }

  // 이 방식대로 하면 영역이 0개일때 seg fault
  /*
  sort(size_vector.begin(), size_vector.end());
  cout << grid_cnt << '\n';
  for (int i = 0; i < K; i++) {
    if (size_vector[i] != 0) {
      cout << size_vector[i] << " ";
    }
  }
  */

  cout << grid_cnt << '\n';
  while (!size_pq.empty()) {
    cout << size_pq.top() << " ";
    size_pq.pop();
  }
}

void dfs(int x, int y, int* size_ptr) {
  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
    if (grid[ny][nx] == 0 && !visited[ny][nx]) {
      visited[ny][nx] = true;
      (*size_ptr) += 1;
      dfs(nx, ny, size_ptr);
    }
  }
}

int bfs(queue<pair<int, int>> q) {
  int size = 1;
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    for (int k = 0; k < 4; k++) {
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      if (ny > M || nx > N || nx < 1 || ny < 1) continue;

      // 칠해지지 않은 영역이고
      // 방문하지 않았다면
      // 영역의 크기를 1 늘리고
      // 탐색 지속
      if (grid[ny][nx] == 0 && !visited[ny][nx]) {
        q.push(make_pair(ny, nx));
        size++;
        visited[ny][nx] = true;
      }
    }
  }

  return size;
}