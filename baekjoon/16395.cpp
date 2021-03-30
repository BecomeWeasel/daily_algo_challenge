#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;

#define N_MAX 31


int pascal[N_MAX][N_MAX];

int k, n;

int ans();

int main(void) {
  cin >> n >> k;

  cout << ans();
}

int ans() {

  fill(pascal[0],pascal[0]+N_MAX*N_MAX,1);
  for (int i = 2; i <= n; i++) {

    for (int j = 2; j <i; j++) {
      pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j];
    }
  }
  return pascal[n][k];
}