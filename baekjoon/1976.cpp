#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define N_MAX 201

int N, M;

// MST를 구성해서 여행계획을 확인함
// 만약 그래프에 MST가 두개이상 나오고
// 한개의 MST에서 다른 MST를 방문하려하면 실패함
bool connected[N_MAX][N_MAX];
vector<int> plan;
int parent[N_MAX];
bool visited[N_MAX];

void ans();

void bfs(queue<int>);

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
  x = Find(x);
  y = Find(y);
  if (x != y) {
    parent[y] = x;
  }
}

int main(void) {
  cin >> N;
  cin >> M;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> connected[i][j];
      connected[j][i] = connected[i][j];
    }
  }

  // 여행계획을 vector에 넣음
  for (int i = 0; i < M; i++) {
    int tmp;
    cin >> tmp;
    plan.push_back(tmp);
  }
  ans();
}

void ans() {
  for (int i = 1; i <= N; i++) {
    parent[i] = i;
  }

  // bfs 탐색으로 MST 만듬
  for (int i = 1; i <= N; i++) {
    if (!visited[i]) {
      queue<int> q;
      visited[i] = true;
      q.push(i);
      bfs(q);
    }
  }

  // 이전에 방문했던 도시와 다음에 방문할 도시가 
  // 서로 다른 set에 있다면 
  // 두 set을 연결하는 다리가 없으니 움직일수 없음
  for (int i = 1; i < M; i++) {
    if (Find(plan[i]) != Find(plan[i - 1])) {
      cout << "NO";
      return;
    }
  }
  cout << "YES";
}

void bfs(queue<int> q) {
  while (!q.empty()) {
    int front = q.front();
    q.pop();

    for (int i = 1; i <= N; i++) {
      if (connected[front][i] && !visited[i]) {
        visited[i] = true;
        q.push(i);
        Union(front, i);
      }
    }
  }
}
