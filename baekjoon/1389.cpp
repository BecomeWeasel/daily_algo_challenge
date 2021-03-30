#include <iostream>
#include <stack>
#include <vector>

using namespace std;
#define FR_MAX 101

int N, M;
int min_person = 1;

vector<vector<int>> kevin(FR_MAX, vector<int>(FR_MAX, 0));

vector<vector<int>> relation(FR_MAX, vector<int>(FR_MAX, 0));

int ans();

void floyd();

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int src, dest;
    cin >> src >> dest;
    relation[src - 1][dest - 1] = 1;
    relation[dest - 1][src - 1] = 1;
  }
  cout << ans();
}

int ans() {
  floyd();
  vector<int> kevin_value(N, 0);
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (i == j) continue;
      kevin_value[i] += relation[i][j];
    }
  }
  
  for (int i = 0; i < N; i++) {
    if (kevin_value[min_person-1] > kevin_value[i]) min_person = i + 1;
  }
  return min_person;
}

void floyd() {


  for (int k = 0; k < N; k++) {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (i == j)
          continue;
        else if (relation[i][k] != 0 && relation[k][j] != 0) {
          if (relation[i][j] == 0)
            relation[i][j] = relation[i][k] + relation[k][j];
          else
            relation[i][j] =
                min(relation[i][j], relation[i][k] + relation[k][j]);
        }
      }
    }
  }
  
}