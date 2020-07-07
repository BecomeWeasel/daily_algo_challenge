#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

#define N_MAX 10001

int N, M, virus_max, virus_max_qt;

// int들을 모아놓은 벡터가 아니라 vector<int>들을 N_MAX개 모아놓은것
// vector<int> array임
vector<int> trust_ll[N_MAX];
vector<bool> visited(N_MAX, false);

void ans();

int bfs(queue<int>, vector<bool>);

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int src, dest;
    cin >> src >> dest;
    trust_ll[dest].push_back(src);
  }
  ans();
}

void ans() {
  vector<int> virus_max_set(N);
  virus_max = -1;
  virus_max_qt = 0;
  for (int i = 1; i <= N; i++) {
    // 1부터 N까지 i번 컴퓨터로 인해
    // 몇개의 컴퓨터가 감염이 되는지 시도
    queue<int> q;
    vector<bool> is_visited(N+1, false);

    q.push(i);
    is_visited[i] = true;

    // i번 컴퓨터로 인해서 총 몇대의 컴퓨터가 감염되는지
    int cnt = bfs(q, is_visited);

    if (virus_max < cnt) {
      virus_max = cnt;
      virus_max_qt = 0;
      virus_max_set[virus_max_qt++] = i;
    } else if (virus_max == cnt) {
      virus_max_set[virus_max_qt++] = i;
    }
  }
  for (int i = 0; i < virus_max_qt; i++) {
    cout << virus_max_set[i] << " ";
  }
}

int bfs(queue<int> q, vector<bool> is_visited) {
  int cnt = 1;
  while (!q.empty()) {
    int front = q.front();
    q.pop();

    for (int i = 0; i < trust_ll[front].size(); i++) {
      // i번재 컴퓨터가 front를 신뢰할수 있으면
      if(!is_visited[trust_ll[front][i]]){
        is_visited[trust_ll[front][i]]=true;
        q.push(trust_ll[front][i]);
        cnt++;
      }
    }
  }
  return cnt;
}
