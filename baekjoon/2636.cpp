#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define MAP_SIZE_MAX 101

int N, M, melting_time, last_cheese;
int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
int copy_map[MAP_SIZE_MAX][MAP_SIZE_MAX];
bool visited[MAP_SIZE_MAX][MAP_SIZE_MAX];
queue<pair<int, int>> melting_target;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void ans();

void boarder_bfs(queue<pair<int, int>>);

int bfs(queue<pair<int, int>>);

int main(void) {
  cin >> N >> M;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      cin >> map[i][j];
    }
  }

  ans();
}

void melting() {
  // 가장자리의 치즈들을 녹임
  while (!melting_target.empty()) {
    pair<int, int> front = melting_target.front();
    melting_target.pop();
    map[front.first][front.second] = 0;
  }
}

void ans() {
  int current_cheese = 0;
  last_cheese = melting_time = 0;
  while (true) {
    memset(visited, false, sizeof(visited));
    current_cheese = 0;
    // 일단 치즈의 개수를 셈
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= M; j++) {
        if (!visited[i][j] && map[i][j] == 1) {
          queue<pair<int, int>> q;
          q.push(make_pair(i, j));
          visited[i][j] = true;


          // 치즈 덩이에서 발견한 치즈개수를 계속 더함
          current_cheese += bfs(q);
        }
      }
    }

    // 남은 치즈가 없다는건
    // 이전타임에 치즈가 다 녹았으니
    // 출력하고 함수를 while을 끝냄
    if (current_cheese == 0) {
      cout << melting_time << '\n' << last_cheese;
      break;
    }

    last_cheese = current_cheese;

    memset(visited, false, sizeof(visited));
    // 치즈의 가장자리를 판단함 (1,1)에는 치즈가 무조건 없으니
    // (1,1)부터 시작
    queue<pair<int, int>> q;
    q.push(make_pair(1, 1));

    // 가장자리에 위치한 치즈를 찾기위한 탐색
    boarder_bfs(q);

    /*
    cout << '\n';
    cout << '\n';
    cout << '\n';
    cout << '\n';
    */

   // 가장자리의 치즈를 녹임
    melting();

    /*
    cout << "********after melting********'\n";
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= M; j++) {
        cout << map[i][j] << " ";
      }
      cout << '\n';
    }
    */
    melting_time++;
  }
  return;
}

// 치즈의 개수를 세기
int bfs(queue<pair<int, int>> q) {
  int cnt = 1;
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    for (int k = 0; k < 4; k++) {
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      if (ny > N || nx > M || ny < 1 || nx < 1) continue;

      if (!visited[ny][nx] && map[ny][nx] == 1) {
        visited[ny][nx] = true;
        q.push(make_pair(ny, nx));
        cnt++;
      }
    }
  }

  // 치즈 개수 리턴
  return cnt;
}

void boarder_bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    for (int k = 0; k < 4; k++) {
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      if (ny > N || nx > M || ny < 1 || nx < 1) continue;

      // 치즈가 아닌 것을 발견했으면 탐색에 추가
      if (!visited[ny][nx] && map[ny][nx] == 0) {
        q.push(make_pair(ny, nx));
        visited[ny][nx] = true;
      }
      // 가장자리 치즈를 발견했을때는
      // melting 함수에서 치즈를 녹여야 하니 queue에 추가
      else if (!visited[ny][nx] && map[ny][nx] == 1) {
        melting_target.push(make_pair(ny, nx));
        visited[ny][nx] = true;
      }
    }
  }
}
