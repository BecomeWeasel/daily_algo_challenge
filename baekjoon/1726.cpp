#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define BOARD_SIZE_MAX 101

struct robot_pos {
  int y;
  int x;
  int cnt;
  int direction;
};

robot_pos start_pos, dest_pos;

int N, M;
int map[BOARD_SIZE_MAX][BOARD_SIZE_MAX];
bool visited[BOARD_SIZE_MAX][BOARD_SIZE_MAX][5];

int ans();

int bfs(queue<robot_pos>);

int main(void) {
  cin >> M >> N;
  for (int i = 1; i <= M; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> map[i][j];
    }
  }
  int sy, sx, sdir;
  cin >> sy >> sx >> sdir;
  start_pos = {sy, sx, 0, sdir};

  int dy, dx, ddir;
  cin >> dy >> dx >> ddir;
  dest_pos = {dy, dx, 0, ddir};

  cout << ans();
}

int ans() {
  queue<robot_pos> q;
  visited[start_pos.y][start_pos.x][start_pos.direction] = true;
  q.push(start_pos);

  return bfs(q);
}

int bfs(queue<robot_pos> q) {
  while (!q.empty()) {
    robot_pos front = q.front();
    q.pop();

    if (front.y == dest_pos.y && front.x == dest_pos.x &&
        front.direction == dest_pos.direction) {
      return front.cnt;
    }

    robot_pos movement;

    // 일단 이동 먼저

    switch (front.direction) {
      // 동쪽을 바라볼때
      case 1:

        // 3칸 움직이는게 1칸씩 세번 움직이는것보다
        // 명령을 덜쓰기 때문에 3칸 먼저 움직임
        for (int i = 1; i <= 3; i++) {
          int ny = front.y;
          int nx = front.x + i;

          if (ny <= 0 || nx <= 0 || nx > N || ny > M) continue;

          if (map[ny][nx] != 0) break;

          // 새로운 칸에 궤도가 있고,방문하지 않았으면
          if (map[ny][nx] != 1 && !visited[ny][nx][front.direction]) {
            visited[ny][nx][front.direction] = true;
            movement = {ny, nx, front.cnt + 1, front.direction};
            q.push(movement);
          }
        }

        // 왼쪽으로 돌기
        if (!visited[front.y][front.x][4]) {
          movement = {front.y, front.x, front.cnt + 1, 4};
          visited[front.y][front.x][4] = true;
          q.push(movement);
        }

        // 오른쪽으로 돌기
        if (!visited[front.y][front.x][3]) {
          movement = {front.y, front.x, front.cnt + 1, 3};
          visited[front.y][front.x][3] = true;
          q.push(movement);
        }

        break;

      // 서쪽을 바라볼때
      case 2:

        // if (front.x - 1 <= 0 && map[front.y][front.x - 1] == 1) break;

        // 3칸 움직이는게 1칸씩 세번 움직이는것보다
        // 명령을 덜쓰기 때문에 3칸 먼저 움직임
        for (int i = 1; i <= 3; i++) {
          int ny = front.y;
          int nx = front.x - i;

          if (ny <= 0 || nx <= 0 || nx > N || ny > M) continue;

          if (map[ny][nx] != 0) break;

          // 새로운 칸에 궤도가 있고,방문하지 않았으면
          if (map[ny][nx] != 1 && !visited[ny][nx][front.direction]) {
            visited[ny][nx][front.direction] = true;
            movement = {ny, nx, front.cnt + 1, front.direction};
            q.push(movement);
          }
        }
        // 왼쪽으로 돌기
        if (!visited[front.y][front.x][3]) {
          movement = {front.y, front.x, front.cnt + 1, 3};
          visited[front.y][front.x][3] = true;
          q.push(movement);
        }

        // 오른쪽으로 돌기
        if (!visited[front.y][front.x][4]) {
          movement = {front.y, front.x, front.cnt + 1, 4};
          visited[front.y][front.x][4] = true;
          q.push(movement);
        }
        break;

      // 남쪽을 바라볼때
      case 3:
        // if (front.y + 1 > N && map[front.y + 1][front.x] == 1) break;

        // 3칸 움직이는게 1칸씩 세번 움직이는것보다
        // 명령을 덜쓰기 때문에 3칸 먼저 움직임
        for (int i = 1; i <= 3; i++) {
          int ny = front.y + i;
          int nx = front.x;

          if (ny <= 0 || nx <= 0 || nx > N || ny > M) continue;

          if (map[ny][nx] != 0) break;

          // 새로운 칸에 궤도가 있고,방문하지 않았으면
          if (map[ny][nx] != 1 && !visited[ny][nx][front.direction]) {
            visited[ny][nx][front.direction] = true;
            movement = {ny, nx, front.cnt + 1, front.direction};
            q.push(movement);
          }
        }
        // 왼쪽으로 돌기
        if (!visited[front.y][front.x][1]) {
          movement = {front.y, front.x, front.cnt + 1, 1};
          visited[front.y][front.x][1] = true;
          q.push(movement);
        }

        // 오른쪽으로 돌기
        if (!visited[front.y][front.x][2]) {
          movement = {front.y, front.x, front.cnt + 1, 2};
          visited[front.y][front.x][2] = true;
          q.push(movement);
        }
        break;

      // 북쪽을 바라볼때
      case 4:
        // if (front.y - 1 < 0 && map[front.y - 1][front.x] == 1) break;

        // 3칸 움직이는게 1칸씩 세번 움직이는것보다
        // 명령을 덜쓰기 때문에 3칸 먼저 움직임
        for (int i = 1; i <= 3; i++) {
          int ny = front.y - i;
          int nx = front.x;

          if (ny <= 0 || nx <= 0 || nx > N || ny > M) continue;

          if (map[ny][nx] != 0) break;

          // 새로운 칸에 궤도가 있고,방문하지 않았으면
          if (map[ny][nx] != 1 && !visited[ny][nx][front.direction]) {
            visited[ny][nx][front.direction] = true;
            movement = {ny, nx, front.cnt + 1, front.direction};
            q.push(movement);
          }
        }
        // 왼쪽으로 돌기
        if (!visited[front.y][front.x][2]) {
          movement = {front.y, front.x, front.cnt + 1, 2};
          visited[front.y][front.x][2] = true;
          q.push(movement);
        }

        // 오른쪽으로 돌기
        if (!visited[front.y][front.x][1]) {
          movement = {front.y, front.x, front.cnt + 1, 1};
          visited[front.y][front.x][1] = true;
          q.push(movement);
        }
        break;
    }
  }
}
