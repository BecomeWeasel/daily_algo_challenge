#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define STORE_MAX 100

int store_cnt;
pair<int, int> store[STORE_MAX];
bool visited[STORE_MAX];
pair<int, int> start_point, end_point;

string ans();

int bfs(queue<pair<int, int>>);

int main(void) {
  int test_num;
  cin >> test_num;
  while (test_num--) {
    memset(store, 0, sizeof(store));
    memset(visited, false, sizeof(visited));

    cin >> store_cnt;
    int x, y;
    cin >> x >> y;
    start_point.first = y;
    start_point.second = x;

    for (int i = 0; i < store_cnt; i++) {
      cin >> x >> y;
      store[i].first = y;
      store[i].second = x;
    }

    cin >> x >> y;
    end_point.first = y;
    end_point.second = x;

    cout << ans() << '\n';
  }
}

string ans() {
  queue<pair<int, int>> q;
  q.push(start_point);
  int result = bfs(q);

  if (result) {
    return "happy";
  } else {
    return "sad";
  }
}

int bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    int y = q.front().first;
    int x = q.front().second;

    q.pop();

    // 지금 좌표에서
    // 남은 맥주를 가지고 페스티벌에 도착할수 있으면
    // 성공
    int diffy = (int)abs(y - end_point.first);
    int diffx = (int)abs(x - end_point.second);

    if (diffy + diffx <= 1000) {
      return 1;
    }

    for (int i = 0; i < store_cnt; i++) {
      if (!visited[i]) {

        // 다음 편의점까지 거리가 1000미터 내라면
        // 무조건 도달할수 있음
        // 그 편의점에서 다시 탐색
        int diffy = (int)abs(y - store[i].first);
        int diffx = (int)abs(x - store[i].second);
        if (diffx + diffy <= 1000) {
          q.push(store[i]);
          visited[i] = true;
        }
      }
    }
  }

  return 0;
}