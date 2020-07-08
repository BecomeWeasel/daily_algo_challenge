#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 100

int N, min_dist, area_cnt;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
vector<vector<int>> map(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));
vector<vector<int>> visited(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));
vector<vector<int>> empty_visited(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));

int ans();

void area_bfs(queue<pair<int, int>>, int);

void bridge_bfs(queue<pair<pair<int, int>, int>>, int);

bool is_border(int, int);

int main(void) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> map[i][j];
    }
  }
  cout << ans();
}

int ans() {
  min_dist = 100000;
  area_cnt = 0;

  // 섬에 이름 붙이는 과정
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (map[i][j] == 1 && !visited[i][j]) {
        queue<pair<int, int>> q;
        visited[i][j] = true;
        map[i][j] = ++area_cnt;

        q.push(make_pair(i, j));
        area_bfs(q, area_cnt);
      }
    }
  }

  /* 섬의 이름이 잘 붙어 있는지 확인
  cout << endl;
  cout << endl;
  cout << endl;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cout << map[i][j] << " ";
    }
    cout << endl;
  }
  */

  // 섬들의 가장자리에서 다른 섬들을 찾는 과정
  // 섬들의 가장자리라는 기준은 상하좌우의 값중에 하나라도 0(바다)라면 섬의
  // 가장자리임
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (map[i][j] != 0 && is_border(i, j)) {
        visited=empty_visited;
        // 섬의 가장자리일때
        queue<pair<pair<int, int>, int>> q;
        q.push(make_pair(make_pair(i, j), 0));
        visited[i][j] = true;

        // 두번째 인자는 현재 섬의 이름
        bridge_bfs(q, map[i][j]);
      }
    }
  }

  // 도착한 다른 섬까지의 거리를 포함하니 
  // 하나 작은 값 리턴
  return min_dist-1;
}


void area_bfs(queue<pair<int, int>> q, int area_label) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    for (int i = 0; i < 4; i++) {
      int ny = front.first + dy[i];
      int nx = front.second + dx[i];

      if (ny >= N || nx >= N || nx < 0 || ny < 0) continue;

      // 발견한 육지에 섬의 이름 붙이기
      if (!visited[ny][nx] && map[ny][nx] == 1) {
        visited[ny][nx] = true;
        map[ny][nx] = area_label;
        q.push(make_pair(ny, nx));
      }
    }
  }
}

void bridge_bfs(queue<pair<pair<int, int>, int>> q, int area_label) {
  while (!q.empty()) {
    pair<pair<int, int>, int> front = q.front();
    q.pop();

    // 도착한곳이 바다가 아니고 ( > 0 )
    // 다른 섬이라면 ( != area_label)
    if (map[front.first.first][front.first.second] > 0 &&
        map[front.first.first][front.first.second] != area_label) {
      // 다리 길이 업데이트
      min_dist = min(min_dist, front.second);
    }

    for (int i = 0; i < 4; i++) {
      int ny = front.first.first + dy[i];
      int nx = front.first.second + dx[i];

      if (ny >= N || nx >= N || nx < 0 || ny < 0) continue;

      // 방문하지 않았고 출발섬이랑 이름이 다른 섬이거나
      // 아예 바다여야함(다리를 하나 놓으니)
      if (!visited[ny][nx] && map[ny][nx] != area_label) {
        visited[ny][nx] = true;
        q.push(make_pair(make_pair(ny, nx), front.second + 1));
      }
    }
  }
}

bool is_border(int y, int x) {
  // 주어진 좌표의 육지가 섬의 가장자리라면
  // 4 방향 근처로 바다가 하나라도 있어야함
  // 4 방향 근처 모두 곱했을때 0이 되면 가장자리임
  int pi = 1;
  for (int k = 0; k < 4; k++) {
    int ny = y + dy[k];
    int nx = x + dx[k];

    if (ny >= N || nx >= N || nx < 0 || ny < 0) continue;
    pi *= map[ny][nx];
  }
  return pi == 0;
}