#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define BOARD_SIZE_MAX 200

// 위치 정보와 횟수,나이트 움직임을 가지는 구조체
struct Monkey_position {
  int y;
  int x;
  int cnt;
  int knight_move;
};

int map[BOARD_SIZE_MAX][BOARD_SIZE_MAX];
// 능력을 몇번 사용했는지도 visited 배열에 중요
bool visited[31][BOARD_SIZE_MAX][BOARD_SIZE_MAX];

pair<int, int> src, dest;

int dy[12] = {-1, -2, -2, -1, 1, 2, 2, 1, -1, 1, 0, 0};
int dx[12] = {-2, -1, 1, 2, -2, -1, 1, 2, 0, 0, -1, 1};

int W, H, K;

int ans();

int bfs(queue<Monkey_position>);

int main(void) {
  cin >> K >> W >> H;
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      cin >> map[i][j];
    }
  }
  cout << ans();
}

int ans() {
  src = make_pair(0, 0);

  dest = make_pair(H - 1, W - 1);

  queue<Monkey_position> Monkey_q;
  Monkey_q.push({src.first, src.second, 0, 0});
  visited[0][0][0] = true;

  return bfs(Monkey_q);
}

int bfs(queue<Monkey_position> q) {
  while (!q.empty()) {
    Monkey_position front = q.front();
    q.pop();
    if (front.y == dest.first && front.x == dest.second) {
      return front.cnt;
    }
    // 나이트처럼 움직일수 있을때
    if (front.knight_move < K) {
      for (int i = 0; i < 8; i++) {
        int ny = front.y + dy[i];
        int nx = front.x + dx[i];
        if (ny >= H || nx >= W || nx < 0 || ny < 0) continue;

        if (map[ny][nx] != 1 && !visited[front.knight_move + 1][ny][nx]) {
          visited[front.knight_move + 1][ny][nx] = true;
          Monkey_position pos;
          pos = {ny, nx, front.cnt + 1, front.knight_move + 1};
          q.push(pos);
        }
      }
    }

    // 나이트처럼 안움직이거나
    // 나이트처럼 움직일 수 없을때
    for (int i = 8; i < 12; i++) {
      int ny = front.y + dy[i];
      int nx = front.x + dx[i];
      if (ny >= H || nx >= W || nx < 0 || ny < 0) continue;

      if (map[ny][nx] != 1 && !visited[front.knight_move][ny][nx]) {
        visited[front.knight_move][ny][nx] = true;
        Monkey_position pos;
        pos = {ny, nx, front.cnt + 1, front.knight_move};
        q.push(pos);
      }
    }
  }
  return -1;
}