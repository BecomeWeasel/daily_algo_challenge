#include <iostream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define NODE_MAX 1001
#define EDGE_MAX 10001

int N, M, V;
vector<vector<bool>> connect(NODE_MAX, vector<bool>(NODE_MAX, false));
vector<bool> visited_dfs(NODE_MAX, false);
vector<bool> visited_bfs(NODE_MAX, false);

void ans();

void dfs(int, int);

void bfs(int, int, queue<int>);

int main(void) {
  cin >> N >> M >> V;
  for (int i = 0; i < M; i++) {
    int src, dest;
    cin >> src >> dest;
    connect[src][dest] = true;
    connect[dest][src] = true;
  }
  ans();
}

void ans() {
  // dfs
  visited_dfs[V] = true;
  dfs(V, V);
  cout << endl;
  // bfs
  queue<int> q;
  q.push(V);
  visited_bfs[V] = true;
  bfs(V, V, q);
}
void dfs(int src, int dest) {
  cout << dest << ' ';
  for (int i = 1; i <= N; i++) {
    if (connect[dest][i] && !visited_dfs[i]) {
      visited_dfs[i] = true;
      dfs(dest, i);
      // visited_dfs[i] = false;
    }
  }
}

void bfs(int src, int dest, queue<int> q) {
  while (!q.empty()) {
    int front = q.front();
    q.pop();

    cout << front << ' ';
    for (int i = 1; i <= N; i++) {
      if (connect[front][i] && !visited_bfs[i]) {
        q.push(i);
        visited_bfs[i] = true;
      }
    }
  }
}