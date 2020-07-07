#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 30
#define WALL -1
#define EMPTY 0
#define POS 1
#define OUT 2

// 3차원을 표현하기 위해 구조체 선언
struct Position {
  int z;
  int y;
  int x;
};

int L, R, C;
Position startPos;

// 북, 남 , 서, 동 , 상 , 하 순서대로 탐색
int dz[6] = {0, 0, 0, 0, -1, 1};
int dy[6] = {-1, 1, 0, 0, 0, 0};
int dx[6] = {0, 0, -1, 1, 0, 0};

// 3차원 벡터
vector<vector<vector<int>>> map(
    MAP_SIZE_MAX,
    vector<vector<int>>(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0)));
vector<vector<vector<int>>> empty_map(
    MAP_SIZE_MAX,
    vector<vector<int>>(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0)));

vector<vector<vector<bool>>> visited(
    MAP_SIZE_MAX,
    vector<vector<bool>>(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false)));
vector<vector<vector<bool>>> empty_visited(
    MAP_SIZE_MAX,
    vector<vector<bool>>(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false)));

void ans();

int bfs(queue<pair<Position, int>>);

int main(void) {
  while (true) {
    // map과 visited 배열 원상태로 돌려놓기
    map = empty_map;
    visited = empty_visited;

    cin >> L >> R >> C;

    // 입력에 하나라도 0이 있으면 종료
    if ((L * R * C) == 0) break;

    for (int i = 0; i < L; i++) {
      for (int j = 0; j < R; j++) {
        string s;
        cin >> s;
        for (int k = 0; k < C; k++) {
          switch (s[k]) {
            case '#':
              map[i][j][k] = -1;
              break;
            case '.':
              map[i][j][k] = 0;
              break;
            case 'S':
              map[i][j][k] = 1;
              // 처음 시작할때 S를 빠르게 찾기 위해서
              startPos = {i, j, k};
              break;
            case 'E':
              map[i][j][k] = 2;
              break;
            default:
              break;
          }
        }
      }
    }
    ans();
  }
}

void ans() {
  queue<pair<Position, int>> q;
  q.push(make_pair(startPos, 0));

  // result에는 탈출까지 걸린 시간
  int result = bfs(q);
  if (result != 0)
    cout << "Escaped in " << result << " minute(s).\n";
  else
    cout << "Trapped!\n";
}

int bfs(queue<pair<Position, int>> q) {
  int dist = 0;
  while (!q.empty()) {
    pair<Position, int> front = q.front();
    q.pop();

    // 출구를 찾았다면 걸린 시간을 바로 리턴
    if (map[front.first.z][front.first.y][front.first.x] == OUT) {
      return front.second;
    }

    // 북, 남 , 서, 동 , 상 , 하 순서대로 탐색
    for (int i = 0; i < 6; i++) {
      int nz = front.first.z + dz[i];
      int ny = front.first.y + dy[i];
      int nx = front.first.x + dx[i];


      if (nx < 0 || ny < 0 || nz < 0 || nx >= C || ny >= R || nz >= L) continue;

      // 지나갈수 있는 곳이고 방문하지 않았다면 탐색함
      if (map[nz][ny][nx] != WALL && !visited[nz][ny][nx]) {
        Position newPos = {nz, ny, nx};
        visited[nz][ny][nx] = true;
        q.push(make_pair(newPos, front.second + 1));
      }
    }
  }
  return dist;
}