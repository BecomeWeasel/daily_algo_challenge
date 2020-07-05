#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 300

int N, M;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

vector<vector<int>> map(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));
vector<vector<bool>> visited(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));

void bfs(queue<pair<int, int>>);

int ans();

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> map[i][j];
    }
  }
  cout << ans();
}

int ans() {
  int year = 0;
  // bfs로 빙산 개수 탐색 후 녹임
  int cnt;
  while (true) {
    cnt = 0;

    // 테두리 부분은 무조건 바다이므로 탐색에서 제외
    for (int i = 1; i < N - 1; i++) {
      for (int j = 1; j < M - 1; j++) {
        if (map[i][j] != 0 && !visited[i][j]) {
          // 이미 빙산이 1개인데 탐색 안된 빙산을 발견하면
          // 무조건 빙산은 2개이므로 여기서 return
          // 그러니 탐색은 무조건 한번만
          if (cnt == 1) return year;


          queue<pair<int, int>> q;
          q.push(make_pair(i, j));
          visited[i][j] = true;
          bfs(q);
          cnt++;
        }
      }
    }

    // 빙산 녹이고 visited 변수 초기화

    // 빙산을 녹일때 새로운 map으로 복사
    vector<vector<int>> new_map(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));
    new_map = map;

    for (int i = 1; i < N - 1; i++) {
      for (int j = 1; j < M - 1; j++) {
        if (new_map[i][j] != 0) {
          for (int k = 0; k < 4; k++) {
            if (new_map[i][j] == 0) break;
            int nx = j + dx[k];
            int ny = i + dy[k];
            if (nx >= M || ny >= N || nx < 0 || ny < 0) continue;
            
            // 기존의 맵에서 주변에 바다가 있다면
            // 빙산을 한 단계 만큼 낮춤
            if (map[ny][nx] == 0) {
              new_map[i][j] -= 1;
            }
          }
        }

        visited[i][j] = false;
      }
    }
    // 빙산이 녹은후 new_map을 map에 복사
    map = new_map;

    // 모든 얼음이 녹았을때
    // 두덩어리로 분리되지 않으면
    // 0을 출력해야 하기 때문에 모든 얼음 녹은걸 출력
    // 위에 이미 빙산의 개수가 2임을 체크하기때문에
    // 이때는 빙산의 개수가 0 혹은 1
    // 이 부분이 없으면 시간 초과
    bool is_all_melted = true;
    for (int i = 1; i < N - 1; i++) {
      for (int j = 1; j < M - 1; j++) {
        if (map[i][j] != 0) {
          is_all_melted = false;
        }
      }
    }
    if (is_all_melted) return 0;

    year++;
  }
}

void bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();
    for (int i = 0; i < 4; i++) {

      // 네 방향을 돌면서 체크
      int nx = front.second + dx[i];
      int ny = front.first + dy[i];

      // 네 방향 기준으로 빙산이 있으면 q에 추가
      if (nx >= M || ny >= N || nx < 0 || ny < 0) continue;
      if (map[ny][nx] != 0 && !visited[ny][nx]) {
        q.push(make_pair(ny, nx));
        visited[ny][nx] = true;
      }
    }
  }
}