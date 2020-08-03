#include <string.h>

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define N_MAX 300001

// S!=E
int N, M, S, E;

// teleport[i] : i번에서 teleport[i]번으로 이어짐. -1이면 텔레포트가 없음
bool visited[N_MAX];
int teleport[N_MAX];

int ans();

int bfs(queue<pair<int, int>>);

int main(void) {
  memset(teleport, -1, sizeof(teleport));
  memset(visited, false, sizeof(visited));

  cin >> N >> M >> S >> E;

  for (int i = 0; i < M; i++) {
    int src, dest;
    cin >> src >> dest;
    teleport[src] = dest;
  }
  cout << ans();
}

int ans() {
  queue<pair<int, int>> q;
  q.push(make_pair(S, 0));
  visited[S] = true;

  int result = bfs(q);

  return result;
}

int bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    // 텔레포트를 할 수 있고 그 지점을 방문하지 않았다면
    if (teleport[front.first] != -1 && !visited[teleport[front.first]]) {
      // 텔레포트를 해서 도착할 수 있다면
      if (teleport[front.first] == E) {
        // 현재시간에서 텔레포트하는 시간까지 포함해서 결과
        return front.second + 1;
      } else {
        q.push(make_pair(teleport[front.first], front.second + 1));
        visited[teleport[front.first]] = true;
      }
    }
    if (front.first + 1 <= N_MAX && !visited[front.first + 1]) {
      if (front.first + 1 == E) {
        return front.second + 1;
      } else {
        q.push(make_pair(front.first + 1, front.second + 1));
        visited[front.first + 1] = true;
      }
    }
    if (front.first - 1 >= 1 && !visited[front.first - 1]) {
      if (front.first - 1 == E) {
        return front.second + 1;
      } else {
        q.push(make_pair(front.first - 1, front.second + 1));
        visited[front.first - 1] = true;
      }
    }
  }

  return -1;
}