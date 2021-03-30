#include <math.h>
#include <string.h>

#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

#define PRIME_MAX 10000

int T, src, dest;
vector<bool> is_prime(PRIME_MAX, true);
int prime_dist[10000];

// vector<vector<bool>> check(PRIME_MAX,vector<bool>(PRIME_MAX,false));

int ans();

void bfs(queue<int>, vector<bool>);

int main(void) {
  cin >> T;

  // 에라토스테네스 체를 이용해 소수들을 먼저 판별함
  for (int i = 2; i <= PRIME_MAX - 1; i++) {
    if (!is_prime[i]) continue;
    for (int j = i + i; j <= PRIME_MAX - 1; j += i) {
      is_prime[j] = false;
    }
  }

  while (T--) {
    cin >> src >> dest;
    int tmp = ans();
    if (tmp == -1)
      cout << "Impossible";
    else
      cout << tmp;

    cout << '\n';
  }
}

int digit_compare(int a, int b) {
  // 주어진 4자리 숫자들이 자릿수별로 얼마나 차이나는지 검사하는 함수
  int diff = 0;
  for (int i = 0; i <= 3; i++) {
    int a_d, b_d, factor;
    factor = (int)pow(10, 3 - i);

    a_d = a / factor;
    b_d = b / factor;
    if (a_d != b_d) diff++;

    a = a - a_d * factor;
    b = b - b_d * factor;
  }
  return diff;
}

int ans() {
  memset(prime_dist, 0, sizeof(prime_dist[0]) * PRIME_MAX);
  queue<int> q;
  vector<bool> check(PRIME_MAX, false);
  check[src] = true;
  q.push(src);
  bfs(q, check);

  if (src == dest)  // 1033 1033 인 경우 결과는 0임
    return prime_dist[dest];
  else if (prime_dist[dest] == 0)  // 거리가 0이라는 건 도달불가를 의미함
    return -1;
  else
    return prime_dist[dest];
}

void bfs(queue<int> q, vector<bool> check) {
  while (!q.empty()) {
    int front = q.front();
    q.pop();

    for (int i = 1000; i <= PRIME_MAX; i++) {
      // i가 소수이고, 방문하지 않았으며 각 자리들의 차이가 1이하일때
      if (is_prime[i] && !check[i] && digit_compare(front, i) <= 1) {
        check[i] = true;

        // 소수 경로 거리 측정
        prime_dist[i] = prime_dist[front] + 1;
        // dest에 도달했다면 q에 넣지않고 멈춤.
        if (i != dest) q.push(i);
      }
    }
  }
}