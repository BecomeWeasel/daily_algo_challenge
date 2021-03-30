#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define MAP_SIZE_MAX 1001

int N, M;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int map[MAP_SIZE_MAX][MAP_SIZE_MAX];
bool visited[MAP_SIZE_MAX][MAP_SIZE_MAX];

void ans();

int bfs(queue<pair<int, int>>);

int main() {
  memset(map, 0, sizeof(map));
  memset(visited, false, sizeof(visited));

  cin >> M >> N;
  for (int i = 1; i <= M; i++) {
    string s;
    cin>>s;
    
    for (int j = 1; j <= N; j++) {
      map[i][j]=s[j-1]-'0';
    }
  }
  ans();
}

void ans() {
  // 전류는 바깥쪽 흰색 격자에 공급
  for (int i = 1; i <= N; i++) {
    // 가장 윗줄이고 , 그 격자가 전류가 잘 통하는 타일이라면
    if (!visited[1][i] && map[1][i] == 0) {
      visited[1][i] = true;
      queue<pair<int, int>> q;
      q.push(make_pair(1, i));
      int result = bfs(q);
      // 가장 끝줄에 닿는 탐색이 성공했을때
      // YES 출력
      if (result == 1) {
        cout << "YES";
        return;
      }
    }
  }
  // 모든 바깥쪽 흰색격자에서 출발한 전류가
  // 가장 끝줄(inner side)에 닿지 못했을때 
  // NO 출력
  cout << "NO";
}

int bfs(queue<pair<int, int>> q) {
  while (!q.empty()) {
    pair<int, int> front = q.front();
    q.pop();

    for (int k = 0; k < 4; k++) {
      // 4방향 탐색
      int ny = front.first + dy[k];
      int nx = front.second + dx[k];

      if (ny > M || nx > N || ny <= 0 || nx <= 0) continue;

      if (!visited[ny][nx] && map[ny][nx] != 1) {
        // 방문한적 없고 전류가 잘통하는데
        // 가장 끝줄(inner side)면 탐색 종료
        if (map[ny][nx] == 0 && ny == M) {
          return 1;
        }
        // 두 조건중 하나라도 만족하지 못하면
        // 계속 탐색
        else {
          q.push(make_pair(ny, nx));
          visited[ny][nx]=true;
        }
      }
    }
  }
  // 가장 끝줄에 닿지 못하고
  // 탐색 종료
  return -1;
}
