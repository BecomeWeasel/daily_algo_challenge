#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 100000

int N;
int max_weight;

vector<int> rope(MAX, 0);

int ans();

int main(void) {
  max_weight=0;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> rope[i];
  }

  cout << ans();
}

int ans(){
  sort(rope.begin(),rope.begin()+N) ;
  
  for(int i=0;i<N;i++){
    max_weight=max(max_weight,rope[i]*(N-i));
  }

  return max_weight;
}