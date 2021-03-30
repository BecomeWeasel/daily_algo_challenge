#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define BOARD_SIZE_MAX 300

int L;
int dy[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
int dx[8] = {-2, -1, 1, 2, -2, -1, 1, 2};
pair<int, int> start, dest;

vector<vector<bool>> visited(BOARD_SIZE_MAX,
                             vector<bool>(BOARD_SIZE_MAX, false));
vector<vector<bool>> empty_visited(BOARD_SIZE_MAX,
                                   vector<bool>(BOARD_SIZE_MAX, false));

int ans();

int bfs(queue<pair<pair<int, int>, int>>);

int main(void) {
  int test_num;
  cin >> test_num;

  while (test_num--) {
    // 출발지 입력
    visited = empty_visited;

    cin>>L;

    int x, y;
    cin >> x >> y;

    start = make_pair(x, y);

    // 도착지 입력
    cin >> x >> y;
    dest = make_pair(x, y);

    cout << ans() << '\n';
  }
}

int ans() {

  // 첫번째 요소는 위치 두번째는 이동횟수
  queue<pair<pair<int, int>, int>> q;

  q.push(make_pair(start, 0));

  return bfs(q);
}

int bfs(queue<pair<pair<int, int>, int>> q) {
  while (!q.empty()) {
    pair<pair<int, int>, int> front = q.front();
    q.pop();


    // 목표지점에 도착했으면
    if (front.first.first == dest.first &&front.first.second == dest.second) {
      return front.second;
    }

    // 나이트가 이동할수 있는 8가지 경우
    for (int i = 0; i < 8; i++) {
      int nx = front.first.first + dx[i];
      int ny = front.first.second + dy[i];

      if (nx >= L || ny >= L || nx < 0 || ny < 0) continue;

      if (!visited[ny][nx]) {
        q.push(make_pair(make_pair(nx, ny), front.second + 1));
        visited[ny][nx] = true;
      }
    }
  }
}