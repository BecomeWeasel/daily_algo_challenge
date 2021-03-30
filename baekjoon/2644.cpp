#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 101

int N, src, dest, M;
vector<vector<bool>> connection(MAX, vector<bool>(MAX, false));
vector<vector<int>> dist(MAX, vector<int>(MAX, 0));
vector<bool> check(MAX, false);

int ans();

void bfs(queue<int>);

int main(void) {
  cin >> N >> src >> dest >> M;
  for (int i = 0; i < M; i++) {
    int parent, child;
    cin >> parent >> child;
    connection[parent][child] = true;
    connection[child][parent] = true;
  }
  cout << ans();
}

int ans() {
  queue<int> q;
  q.push(src);
  check[src] = true;
  bfs(q);
  if (dist[src][dest] != 0) {
    // 탐색이 완료되어서 촌수가 0에서 다른 수로 바뀌었다면
    // src에서 dest로 가는 연결이 있음
    return dist[src][dest];
  } else
    return -1;
    // 탐색이 끝났는데 촌수가 0 그대로라면
    // src에서 dest로 가는 연결이 없음
}

void bfs(queue<int> q) {
  while (!q.empty()) {
    int front = q.front();
    q.pop();

    for (int i = 1; i <= N; i++) {
      if (connection[front][i] && !check[i]) {
        //front와 i가 연결되어 있고 i를 방문하지 않았다면
        check[i] = true;
        q.push(i);
        dist[src][i] = dist[src][front] + 1;
        // BFS 탐색이니 src-i 거리는 src-front+1
      }
    }
  }
}