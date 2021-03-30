#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define CITY_MAX 100001

int N;
int gas[CITY_MAX];
// city_distance[i] : i-1번째 도시에서 i번째 도시까지 가는 거리
int city_distance[CITY_MAX];

long long ans();

int main(void) {
  cin >> N;
  for (int i = 2; i <= N; i++) {
    cin >> city_distance[i];
  }
  for (int i = 1; i <= N; i++) {
    cin >> gas[i];
  }
  cout << ans();
}

long long ans() {
  long long total_cost = 0;

  int i = 1;
  
  // N-1번째 주유소까지 채울지 말지 결정
  while (i <= N - 1) {
    int expensive_gas, dist;
    
    // exp_gas : i번째 주유소보다 같거나 비싼 금액 주유소의 개수
    // dist : i번째 주유소에서 얼마를 주유할지
    expensive_gas = dist = 0;
    for (int j = i; j <= N - 1; j++) {
      if (gas[i] <= gas[j]) {

        // j번째 주유소가 i번째보다 비싸거나 같다면 j+1번째 도시까지 가기전에 다 채움
        dist += city_distance[j+1];
        expensive_gas++;
      } else {
        break;
      }
    }

    // i번째 주유소에서 사용하는 금액
    // total_cost는 long long이고 gas와 dist는 int니
    // long long으로 implcit conversion이 필요함
    total_cost+=1LL*gas[i]*dist;

    // i번째 주유소보다 저렴한 곳까지 점프
    i+=expensive_gas; 
  }
  return total_cost;
}
