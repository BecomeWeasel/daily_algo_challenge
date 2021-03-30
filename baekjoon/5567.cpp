#include <string.h>

#include <iostream>
#include <queue>

using namespace std;

#define CONNECT_MAX 501

bool connection[CONNECT_MAX][CONNECT_MAX];

int n, m;

int ans();

int main(void) {
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int src, dest;
    cin >> src >> dest;

    connection[src][dest] = connection[dest][src] = true;
  }
  cout << ans();
}

int ans() {
  int cnt = 0;
  bool come[CONNECT_MAX];
  memset(come, false, sizeof(come));

  for (int i = 2; i <= n; i++) {
    // i번째와 상근이가 친구면
    // i는 온다
    if (connection[1][i]) {
      come[i] = true;

      // i와 j가 친구면
      // j도 온다
      for (int j = 2; j <= n; j++) {
        if (i == j) continue;
        if (connection[i][j]) {
          come[j] = true;
        }
      }
    }
  }

  // 결혼식에 오는 사람을 센다
  for (auto e : come) {
    if (e) cnt++;
  }

  return cnt;
}