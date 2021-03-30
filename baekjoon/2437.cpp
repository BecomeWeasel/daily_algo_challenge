#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define N_MAX 1000

int N;
vector<int> weight(N_MAX, 0);

int ans();

int main(void) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> weight[i];
  }
  cout << ans();
}

int ans() {
  sort(weight.begin(), weight.begin()+N);
  int sum=0;
  // sum까지는 무게추로 구성할수 있음
  // 예를 들어 1 1 3 7 10이 있으면
  // 1=1, 2=1+1 :  1 두개의 sum
  // 3=3, 4=1+3, 5=2+3 : 3 무게추 하나로 3 만들고, 4 5는 sum=2일때 3을 더해서 만들수 있음
  // 이때의 sum=5
  // 하지만 그다음 6은 구성할수 없음. 1~5까지는 sum이 5이기 때문에 만들수 있음
  // 그 다음 무게추가 7이기 때문에 1~5까지 만들수 있지만 6은 만들수 없고
  // 1~5 가능 6 불가능 7은 무게추 7 하나로 가능 
  // 나머지도 7+1,7+2,7+3 ... 이렇게 구성가능함
  for(int i=0;i<N;i++){
    if(weight[i]>sum+1) return sum+1;
    sum+=weight[i];
  }
  // 모든 추를 다 사용하고도 그전에 최솟값이 안구해졌다면
  // 추의 무게를 다 더한것 +1이
  // 가장 작은 잴 수 없는 최솟값
  return sum+1;
}