#include <string.h>

#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

struct ball {
  vector<int> light;
  vector<int> heavy;
};

#define BALL_MAX 100

int N, M, half_cnt;
ball balls[BALL_MAX];
int answer[2][BALL_MAX];

// 첫번째 인자 : 현재 노드
// 두번째 인자 : 탐색방향(0이면 작은것,1이면 큰것)
// 세번째 인자 : 개수
// 네번째 인자 : 방문체크 배열
// 다섯번째 인자 : 원 시작 지점
void dfs(int, int, int, bool[], int);

int ans();

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int heavy, light;
    cin >> heavy >> light;
    balls[heavy].light.push_back(light);
    balls[light].heavy.push_back(heavy);
  }
  cout << ans();
}

int ans() {
  memset(answer, 0, sizeof(answer));
  half_cnt = 0;

  for (int i = 1; i <= N; i++) {
    bool visited[BALL_MAX]={false,};
    visited[i] = true;
    dfs(i, 0, 0, visited, i);

    dfs(i, 1, 0, visited, i);
    visited[i] = false;
  }

  for (int i = 0; i < 2; i++) {
    for (int j = 1; j <= N; j++) {
      if (answer[i][j] >= ((N + 1) / 2)) half_cnt++;
    }
  }

  return half_cnt;
}

void dfs(int current, int direction, int cnt, bool visited[], int start) {
  // if (cnt == ((N + 1) / 2)) {
  //   answer[start] = true;
  //   return;
  // }
  if (direction == 0) {
    for (int i = 0; i < balls[current].light.size(); i++) {
      if(!visited[balls[current].light[i]]){
        visited[balls[current].light[i]]=true;
        answer[direction][start]++;
        dfs(balls[current].light[i],direction,cnt+1,visited,start);
      }
    }
  } else {
    for (int i = 0; i < balls[current].heavy.size(); i++) {
      if(!visited[balls[current].heavy[i]]){
        visited[balls[current].heavy[i]]=true;
        answer[direction][start]++;
        dfs(balls[current].heavy[i],direction,cnt+1,visited,start);
      }
    }
  }
  
}
