#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

#define MAP_SIZE_MAX 50
#define WATER -1
#define EMPTY 0
#define GOSMI 1
#define OUT 2
#define ROCK 3

using namespace std;

int R, C;

// 고스미의 위치와 동굴 위치는 빨리 나갈수있게 기록
pair<int, int> startPos, endPos;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

vector<vector<bool>> visited(MAP_SIZE_MAX, vector<bool>(MAP_SIZE_MAX, false));
vector<vector<int>> map(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));

void ans();

// 첫번째 요소는 위치, 두번째는 시간
int bfs(queue<pair<pair<int, int>, int>>);

void flood();

int main(void) {
  cin >> R >> C;
  for (int i = 0; i < R; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < C; j++) {
      switch (s[j]) {
        case '*':
          map[i][j] = WATER;
          break;
        case '.':
          map[i][j] = EMPTY;
          break;
        case 'S':
          map[i][j] = GOSMI;
          startPos = make_pair(i, j);
          break;
        case 'D':
          map[i][j] = OUT;
          endPos = make_pair(i, j);
          break;
        case 'X':
          map[i][j] = ROCK;
          break;
        default:
          break;
      }
    }
  }
  ans();
}

void ans() {
  queue<pair<pair<int, int>, int>> q;

  // 처음위치와 초기 시간을 q에 넣음
  q.push(make_pair(startPos, 0));
  visited[startPos.first][startPos.second] = true;
  int result = bfs(q);

  result != -1 ? cout << result : cout << "KAKTUS";
}

// 물이 확산되게 하는 함수
void flood() {
  // 기존의 map만 사용한다면 물이 계속 번질수 있으니 new_map 변수 사용
  vector<vector<int>> new_map(MAP_SIZE_MAX, vector<int>(MAP_SIZE_MAX, 0));

  // new_map에 기존 map 복사
  new_map = map;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (map[i][j] == WATER) {
        for (int k = 0; k < 4; k++) {
          int ny = i + dy[k];
          int nx = j + dx[k];

          if (ny >= R || nx >= C || nx < 0 || ny < 0) continue;

          // 동굴과 바위는 물에 잠길 수 없음
          if (map[ny][nx] != OUT && map[ny][nx] != ROCK) {
            new_map[ny][nx] = WATER;
          }
        }
      }
    }
  }
  // 업데이트된 지도를 반영
  map = new_map;
}

int bfs(queue<pair<pair<int, int>, int>> q) {
  // while loop을 두개짜서 탈출조건 만듬
  while (!q.empty()) {
    queue<pair<pair<int, int>, int>> tmpQ;
    while (!q.empty()) {
      pair<pair<int, int>, int> front = q.front();
      q.pop();

      // 고슴이가 움직인 위치에 이미 물이 찼으므로 
      //  그 고스미는 직전 시간대에 이동하지 않았어야 함 
      if (map[front.first.first][front.first.second] == WATER) continue;


      // 동굴에 도착해서 탈출했다면
      if (front.first.first == endPos.first &&
          front.first.second == endPos.second) {
        return front.second;
      }

      for (int i = 0; i < 4; i++) {
        int ny = front.first.first + dy[i];
        int nx = front.first.second + dx[i];

        if (nx < 0 || ny < 0 || nx >= C || ny >= R) continue;

        // 일반 Q에 넣으면 이동하고 물이 넘치는걸 표현할수 없음
        // 고스미가 n분에 이동한 후 위치들을 tmpQ에 저장
        if (!visited[ny][nx] && map[ny][nx] != ROCK && map[ny][nx] != WATER) {
          tmpQ.push(make_pair(make_pair(ny, nx), front.second + 1));
          visited[ny][nx] = true;
        }
      }
    }

    // 기존 q에 tmpQ를 복사해서 다음 시간의
    // 고스미의 위치 넣음
    q = tmpQ;

    // 고스미가 물이 잠기는곳으로는 이동할수 없다는
    // 이미 이동한 후에 물이 잠기는 것으로 해석
    flood();
  }

  // 고스미가 다 이동하였는데 동굴을 찾기 못했을때
  return -1;
}