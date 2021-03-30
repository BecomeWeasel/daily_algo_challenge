#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 1000001

int N, M;
int parent[N_MAX];

void ans();

int Find(int x) {
  if (x == parent[x])
    return x;

  else {
    int p = Find(parent[x]);
    parent[x] = p;
    return p;
  }
}

void Union(int x, int y) {
  int px = Find(x);
  int py = Find(y);

  if (px != py) {
    parent[py] = px;
  }
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N >> M;
  ans();
}

void ans() {
  for (int i = 1; i <= N; i++) {
    parent[i] = i;
  }
  for (int i = 0; i < M; i++) {
    int op, src, dest;
    cin >> op >> src >> dest;
    if (op == 0) {
      Union(src, dest);
    } else {
      if (Find(src) != Find(dest))
        cout << "NO\n";
      else
        cout << "YES\n";
    }
  }
}
