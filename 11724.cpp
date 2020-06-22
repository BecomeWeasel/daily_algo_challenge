#include <iostream>
#include <vector>

using namespace std;

#define MAX 1001

int N, M,area_count;
vector<vector<bool>> map(MAX, vector<bool>(MAX, false));
vector<bool> visited(MAX, false);

int ans();

void dfs(int, int);

int main(void) {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int u, v;
    cin >> u >> v;
    map[u][v] = map[v][u] = true;
  }
  cout << ans();
}

int ans() {
  area_count=0; 
  for (int i = 1; i <= N; i++) {
    if (!visited[i]) {
      dfs(i, i);
      area_count++;
    }
  }
  return area_count;
}

void dfs(int src,int dest){
  visited[dest]=true;
  for(int i=1;i<=N;i++){
    if(map[dest][i]==true&&!visited[i]){
      dfs(dest,i);
    }
  }
}