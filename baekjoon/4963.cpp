#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 51

int W, H, island;
int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

vector<vector<int>> map(MAX, vector<int>(MAX, -1));
vector<vector<bool>> check(MAX, vector<bool>(MAX, false));

int ans();

void bfs(queue<pair<int, int>>);

int main(void) {
  while (true) {
    island = 0;
    // 섬의 개수
    cin >> W >> H;
    if (W == 0 && H == 0) return 0;
    for (int i = 1; i <= H; i++) {
      for (int j = 1; j <= W; j++) {
        cin >> map[i][j];
      }
    }
    cout << ans()<<'\n';
  }
}

int ans() {
  // 방문한 지역을 기록하는 check 2차원 배열 초기화
  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      check[i][j] = false;
    }
  }

  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      if (map[i][j] == 1 && !check[i][j]) {
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));
        check[i][j] = true;
        island++;
        bfs(q);
      }
    }
  }

  return island;
}

void bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();
    
    // 중앙을 기준으로 8방향을 돌면서 체크
    for (int i = 0; i < 8; i++) {
      int ny = front.first + dy[i];
      int nx = front.second + dx[i];

      if (nx > W || ny > H || ny < 1 || nx < 1) continue;

      // 방문하지 않았고 걸을수 있는 지역이면 q에 push
      if (!check[ny][nx] && map[ny][nx] == 1) {
        q.push(make_pair(ny, nx));
        check[ny][nx] = true;
      }
    }
  }
}