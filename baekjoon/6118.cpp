#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define PLACE_MAX 20001

int N, M, max_dist, max_house, max_cnt;
int house_dist[PLACE_MAX];
vector<vector<int>> connected(PLACE_MAX);
bool visited[PLACE_MAX];

void ans();

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int src, dest;
    cin >> src >> dest;

    connected[src].push_back(dest);
    connected[dest].push_back(src);
  }
  ans();
}

void dfs(int src, int dist) {
  house_dist[src] = min(dist, house_dist[src]);

  // 이렇게 찾으면 모든 점에 대해서 dfs 탐색이
  // 온전히 끝나지 않은 상태에서 가장 큰 거리 값을 가지니 무의미
  // max_dist = max(max_dist, dist);

  for (int i = 2; i <= N; i++) {
    // connected는 인접리스트로 구현
    // src와 i가 연결되어 있으면
    for (int j = 0; j < connected[src].size(); j++) {
      if (connected[src][j] == i && !visited[i]) {
        visited[i] = true;
        dfs(i, dist + 1);
        visited[i] = false;
      }
    }
  }
}

void bfs(queue<int> q) {
  while (!q.empty()) {
    int front = q.front();
    q.pop();

    if (max_dist < house_dist[front]) {
      max_dist = house_dist[front];
      max_cnt = 1;
      max_house = front;
    } else if (max_dist == house_dist[front]) {
      max_cnt++;
      if (max_house > front) {
        max_house = front;
      }
    }


    /*
    // 이렇게 구현하면 
    // 인접리스트로 구현했을때 connected[front].size()개수 만큼 탐색할수 있는데
    // 굳이 2번부터 N번까지 탐색을 해야하니 시간 초과
    for (int i = 2; i <= N; i++) {
      // connected는 인접리스트로 구현
      // src와 i가 연결되어 있으면
      for (int j = 0; j < connected[front].size(); j++) {
        if (connected[front][j] == i && !visited[i]) {
          visited[i] = true;
          q.push(i);
          house_dist[i] = house_dist[front] + 1;
        }
      }
    }
    */

    // connected는 인접리스트로 구현
    // src와 connected[front][j]가 연결되어 있고
    // 방문하지 않았다면
    // 그 점에 대해서 dist를 +1 해주고
    // 다시 탐색시작
    for (int j = 0; j < connected[front].size(); j++) {
      if (!visited[connected[front][j]]) {
        visited[connected[front][j]] = true;
        q.push(connected[front][j]);
        house_dist[connected[front][j]] = house_dist[front] + 1;
      }
    }
  }
}

void ans() {
  memset(visited, false, sizeof(visited));
  memset(house_dist, 0, sizeof(house_dist));

  /*
    int hide, max_cnt;
    max_dist = 0;
    // 숨을 곳 초기상태 0
    hide = 0;
    max_cnt = 0;
  */

  house_dist[1] = 0;

  max_dist = 0;
  max_house = 0;
  max_cnt = 0;

  // dfs 구현시 시간초과
  // dfs(1, 0);
  queue<int> q;
  q.push(1);
  visited[1] = true;

  bfs(q);
  cout << max_house << " " << max_dist << " " << max_cnt;
}
