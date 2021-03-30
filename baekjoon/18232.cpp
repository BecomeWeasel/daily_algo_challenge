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
vector<int> teleport[N_MAX] = {};

int ans();

int bfs(queue<pair<int, int>>);

int main(void) {
  // memset(teleport, -1, sizeof(teleport));
  memset(visited, false, sizeof(visited));

  cin >> N >> M >> S >> E;

  for (int i = 0; i < M; i++) {
    int src, dest;
    cin >> src >> dest;
    teleport[src].push_back(dest);
    teleport[dest].push_back(src);
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

    /*
    if (front.first == E) {
      return front.second;
    }*/

    // 텔레포트를 할 수 있고 그 지점을 방문하지 않았다면
    for (int i = 0; i < teleport[front.first].size(); i++) {
      if (!visited[teleport[front.first][i]]) {
        if (teleport[front.first][i] == E) {
          return front.second + 1;
        } else {
          q.push(make_pair(teleport[front.first][i], front.second + 1));
          visited[teleport[front.first][i]] = true;
        }
      }
    }
    if (front.first + 1 <= N && !visited[front.first + 1]) {
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