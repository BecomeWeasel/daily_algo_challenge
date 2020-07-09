#include <string.h>

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define C_MAX 1001

int N, M;
bool connected[C_MAX][C_MAX];
bool visited[C_MAX];
// MST를 구현할때 kruskal 사용
int parent[C_MAX];

int Find(int x) {
  if (parent[x] == x)
    return x;
  else {
    int p = Find(parent[x]);
    parent[x] = p;
    return p;
  }
}

void Union(int x, int y) {
  int px = Find(x);
  int py = Find(y);

  if (px != py) {
    parent[py] = px;
  }
}

int ans();

int bfs(queue<int>);

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int test_num;
  cin >> test_num;

  while (test_num--) {
    cin >> N >> M;
    memset(connected, false, sizeof(connected));
    memset(visited, false, sizeof(visited));
    memset(parent, 0, sizeof(parent));
    for (int i = 0; i < M; i++) {
      int src, dest;
      cin >> src >> dest;
      connected[src][dest] = connected[dest][src] = true;
    }
    cout << ans() << '\n';
  }
}

int ans() {
  for (int i = 1; i <= N; i++) {
    parent[i] = i;
  }
  int result = 0;

  // bfs를 사용해서 모든 노드들을
  // 가장 적은 간선 개수로 이으려고함
  // MST 
  for (int i = 1; i <= N; i++) {
    if (!visited[i]) {
      queue<int> q;
      visited[i] = true;
      q.push(i);
      result += bfs(q);
    }
  }
  return result;
}

int bfs(queue<int> q) {
  int cnt = 0;
  while (!q.empty()) {
    int front = q.front();
    q.pop();
    for (int i = 1; i <= N; i++) {
      if (connected[front][i] && !visited[i]) {

        // front와 i를 오가는 비행기가 있고
        // i를 방문하지 않았으면 
        // MST의 부분집합에 넣음
        Union(i, front);
        visited[i] = true;
        q.push(i);
        cnt++;
      }
    }
  }
  return cnt;
}