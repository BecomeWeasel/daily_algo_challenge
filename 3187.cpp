#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAP_SIZE_MAX 250
#define FENCE -1
#define EMPTY 0
#define SHEEP 1
#define WOLF 2

int R, C, sheep, wolf;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
vector<vector<int>> map(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));
vector<vector<bool>> visited(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));

void ans();

// bfs 함수가 영역내에서 살아남은 양과 늑대의 개수를 반환
pair<int, int> bfs(queue<pair<int, int>>);

int main(void) {
  cin >> R >> C;
  for (int i = 0; i < R; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < C; j++) {
      switch (s[j]) {
        case '.':
          map[i][j] = EMPTY;
          break;
        case '#':
          map[i][j] = FENCE;
          break;
        case 'v':
          map[i][j] = WOLF;
          break;
        case 'k':
          map[i][j] = SHEEP;
          break;
        default:
          break;
      }
    }
  }
  ans();
}

void ans() {
  sheep = wolf = 0;

  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (map[i][j] != FENCE && !visited[i][j]) {
        queue<pair<int, int>> q;
        visited[i][j] = true;
        q.push(make_pair(i, j));

        pair<int, int> result = bfs(q);
        sheep += result.first;
        wolf += result.second;
      }
    }
  }
  cout << sheep << " " << wolf;
}

pair<int, int> bfs(queue<pair<int, int>> q) {
  pair<int, int> result;
  result.first = result.second = 0;
  while (!q.empty()) {
    // first = 양의 개수 second = 늑대 개수

    pair<int, int> front = q.front();
    q.pop();

    // 현재 탐색중인 위치에 있는 동물이 양인지 늑대인지 파악해서 개수 올림
    switch (map[front.first][front.second]) {
      case SHEEP:
        result.first++;
        break;
      case WOLF:
        result.second++;
        break;
      default:
        break;
    }
    for (int i = 0; i < 4; i++) {
      int ny = front.first + dy[i];
      int nx = front.second + dx[i];

      if (ny >= R || nx >= C || ny < 0 || nx < 0) continue;

      // 펜스를 제외하고는 모두 4방향 (상,하,좌,우) 탐색 
      if (!visited[ny][nx] && map[ny][nx] != FENCE) {
        visited[ny][nx] = true;
        q.push(make_pair(ny, nx));
      }
    }
  }

  // 양이 늑대보다 많을 경우
  if (result.first > result.second) result.second = 0;
  // 그 외 모든 경우
  else
    result.first = 0;

  return result;
}