#include <math.h>

#include <iostream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define MAX 10000

int A, B;
// vector<char> DSLR_OP(MAX);
// vector<bool> visited(MAX);

void ans();

string bfs(queue<pair<int, string>>, bool[], char[]);

int D(int);

int S(int);

int L(int);

int R(int);

int main(void) {
  int test;
  cin >> test;
  while (test--) {
    cin >> A >> B;
    ans();
  }
}

void ans() {
  
  // 전역변수 사용시 다시 초기화하는데 시간 오래걸림
  bool visited[MAX] = {0};
  char DSLR_OP[MAX];
  queue<pair<int, string>> q;
  q.push(make_pair(A, ""));
  visited[A] = true;
  string result = bfs(q, visited, DSLR_OP);

  cout << result << '\n';
  
}

string bfs(queue<pair<int, string>> q, bool visited[], char DSLR_OP[]) {
  while (!q.empty()) {
    pair<int, string> front = q.front();
    q.pop();

    if (front.first == B) {
      return front.second;
    }

    if (!visited[D(front.first)]) {
      DSLR_OP[D(front.first)] = 'D';
      visited[D(front.first)] = true;
      q.push(make_pair(D(front.first), front.second + 'D'));
    }
    if (!visited[S(front.first)]) {
      DSLR_OP[S(front.first)] = 'S';
      visited[S(front.first)] = true;
      q.push(make_pair(S(front.first), front.second + 'S'));
    }
    if (!visited[L(front.first)]) {
      DSLR_OP[L(front.first)] = 'L';
      visited[L(front.first)] = true;
      q.push(make_pair(L(front.first), front.second + 'L'));
    }
    if (!visited[R(front.first)]) {
      DSLR_OP[R(front.first)] = 'R';
      visited[R(front.first)] = true;
      q.push(make_pair(R(front.first), front.second + 'R'));
    }
  }
  return NULL;
}

int D(int a) { return 2 * a <= 9999 ? 2 * a : (2 * a) % 10000; }

int S(int a) { return a != 0 ? a - 1 : 9999; }

int L(int a) { return (a % 1000) * 10 + a / 1000; }

int R(int a) { return (a % 10) * 1000 + (a / 10); }