#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define N_MAX 51

vector<vector<int>> friend_relation(N_MAX, vector<int>(N_MAX, 0));

int N, M, current_friend_relation, added_friend;
vector<int> v_added_friend;

bool is_all_connected();

int add_friend(int, vector<vector<int>>);

void ans();

int main(void) {
  cin >> N >> M;
  current_friend_relation = M;
  for (int i = 0; i < M; i++) {
    int src, dest;
    cin >> src >> dest;
    friend_relation[src][dest] = friend_relation[dest][src] = 1;
  }

  ans();
}

void ans() {
  int K = 0;

  while (!is_all_connected()) {
    added_friend = 0;
    vector<vector<int>> copy_friend_relation(N_MAX, vector<int>(N_MAX, 0));
    copy_friend_relation = friend_relation;
    for (int h = 1; h <= N; h++) {
      int ith_added_friend = 0;
      for (int i = 1; i <= N; i++) {
        if (i == h) continue;
        if (friend_relation[h][i] == 1) {
          for (int j = 1; j <= N; j++) {
            if (friend_relation[i][j] == 1 && copy_friend_relation[h][j] == 0 &&h != j) {
              copy_friend_relation[h][j] = copy_friend_relation[j][h] = 1;
              ith_added_friend++;
            }
          }
        }
      }
      added_friend += ith_added_friend;
    }

    friend_relation = copy_friend_relation;

    current_friend_relation += added_friend;
    v_added_friend.push_back(added_friend);
    K += 1;
  }

  cout << K << '\n';
  for (int i = 0; i < K; i++) {
    cout << v_added_friend[i] << '\n';
  }
}

bool is_all_connected() { return ((N * N) - N) / 2 == current_friend_relation; }