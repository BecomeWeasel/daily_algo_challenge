#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define DAY_MAX 1000001

int N;
int price[DAY_MAX];

long long ans();

int main(void) {
  int test_num;
  cin >> test_num;

  while (test_num--) {
    cin >> N;
    for (int i = 1; i <= N; i++) {
      cin >> price[i];
    }
    cout << ans() << '\n';
  }
}

long long ans() {
  long long profit = 0;

  // 주가를 뒤에서부터 탐색후
  // max 값을 찾는다
  // 그 전날 주가가 max 값보다 작으면
  // 그 전날 사는게 이득이니 
  // profit+=max-price[i-1];
  int max=price[N];
  for(int i=N-1;i>0;i--){
    if(price[i]>max){
      max=price[i];
    }else if(price[i]<max){
      // i 날 주식을 사서 max 날 팔면
      // 이득
      profit+=max-price[i];
    }else{
      // 주가가 max랑 같으면
      // 아무것도 안함
    }
  }

  return profit < 0 ? 0 : profit;
}
