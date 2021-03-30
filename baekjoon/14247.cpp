#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 100001

int tree[N_MAX];
int growth[N_MAX];
int max_tree, max_idx;

int N;

long long ans();

int main(void) {
  cin >> N;
  max_tree = -1;

  for (int i = 1; i <= N; i++) {
    cin >> tree[i];
    if (max_tree < tree[i]) {
      max_tree = tree[i];
      max_idx = i;
    }
  }
  for (int i = 1; i <= N; i++) {
    cin >> growth[i];
  }

  cout << ans();
}

long long ans() {
  long long cut = 0;
  for (int i = 0; i < N; i++) {
    // 가장 큰 나무 자르기
    cut += tree[max_idx];
    // 자른 나무 크기 0으로 만들기
    tree[max_idx] = 0;

    // 나무 성장시키기
    max_tree = -1;

    // 나무를 키우면서 가장 큰 나무를 체크
    for (int j = 1; j <= N; j++) {
      tree[j] += growth[j];
      if (max_tree < tree[j]) {
        max_tree = tree[j];
        max_idx = j;
      }
    }
  }

  return cut;
}
