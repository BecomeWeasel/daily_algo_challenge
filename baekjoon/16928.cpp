#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define LADDER_MAX 15
#define SNAKE_MAX 15

int N, M;
vector<pair<int, int>> ladder(LADDER_MAX);
vector<pair<int, int>> snake(SNAKE_MAX);
bool visited[101];

int ans();

// first : 위치 second : 회수
int bfs(queue<pair<int, int>>);

int check(int);

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    int x, y;
    cin >> x >> y;

    // 사다리의 시작점과 도착점을 기록
    ladder[i] = make_pair(x, y);
  }

  for (int i = 0; i < M; i++) {
    int u, v;
    cin >> u >> v;

    // 뱀의 시작점과 도착점을 기록
    snake[i] = make_pair(u, v);
  }

  cout << ans();
}

int ans() {
  queue<pair<int, int>> q;

  q.push(make_pair(1, 0));
  visited[1] = true;

  return bfs(q);
}

int bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    // 100칸에 도착하면 반환
    if (front.first == 100) {
      return front.second;
    }

    for (int i = 1; i <= 6; i++) {
      // 주사위를 굴렸는데 100을 넘으면 움직이지 않음
      if (front.first + i > 100) continue;

      // 정상적으로 움직일지 뱀 or 사다리를 탈지
      int pos = check(front.first + i);

      // 뱀 or 사다리를 탈때
      // 뱀 or 사다리는 방문제한조건이 없어야함
      // 6연속으로 뱀이 있을 경우에 움직이지 못함
      if (pos != -1 ) {
        visited[pos] = true;
        q.push(make_pair(pos, front.second + 1));
      } 
      // 주사위를 굴려서 움직일때
      else if (!visited[front.first + i]) {
        visited[front.first + i] = true;
        q.push(make_pair(front.first + i, front.second + 1));
      }
    }
  }
  return -1;
}

int check(int pos) {

  for (int i = 0; i < N; i++) {
    // 사다리의 시작점과 일치하면 도착점을 반환
    if (ladder[i].first == pos) return ladder[i].second;
  }
  for (int i = 0; i < M; i++) {
    // 뱀의 시작점과 일치하면 도착점을 반환
    if (snake[i].first == pos) return snake[i].second;
  }

  // 뱀 or 사다리의 입구랑 pos가 일치하지 않음
  return -1;
}