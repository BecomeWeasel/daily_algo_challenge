#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAP_MAX 100001

int N, K;

vector<bool> visited(MAP_MAX, false);

int ans();

// 동생을 찾기 위한 최단 경로를 찾으니 bfs 사용
int bfs(queue<pair<int, int>>);

int main(void) {
  cin >> N >> K;
  cout << ans();
}

int ans() {
  queue<pair<int, int>> q;
  visited[N] = true;

  // 초기 위치와 초기 이동 회수 0을 q에 넣음
  q.push(make_pair(N, 0));
  return bfs(q);
}

int bfs(queue<pair<int, int>> q) {
  // 탐색을 할때 선택가능한 옵션이 
  // 순간이동,한칸뒤로가기,한칸앞으로 가기 모두를 선택해야 하니
  // bfs
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();
    // cout<< "current pos and cnt is "<<front.first<<" "<<front.second<<endl;
    if (front.first == K) {
      return front.second;
    }
    // 먼저 순간이동해서 탐색
    if (front.first * 2 <= MAP_MAX && !visited[front.first * 2]) {
      q.push(make_pair(front.first * 2, front.second + 1));
      visited[front.first * 2] = true;
    }

    // 한칸 뒤로 가서 탐색
    if (front.first - 1 >= 0 && !visited[front.first - 1]) {
      q.push(make_pair(front.first - 1, front.second + 1));
      visited[front.first - 1] = true;
    }

    // 한칸 앞으로 가서 탐색
    if (front.first + 1 <= MAP_MAX && !visited[front.first + 1]) {
      q.push(make_pair(front.first + 1, front.second + 1));
      visited[front.first + 1] = true;
    }
  }
}