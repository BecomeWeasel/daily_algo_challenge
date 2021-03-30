#include <iostream>
#include <queue>

using namespace std;

int N, A, B, C;

// 도우의 가격은 모두 같다.
// 300 100 50의 열량을 가진 세개의 토핑이 있을때
// 토핑의 가격이 같기 때문에 300+50 보다 300+100이 무조건 가성비가 좋다
// 그러므로 열량이 큰 순서대로 쭉 비교하면서 토핑의 개수 N번만큼 비교하면 됨

priority_queue<int> toppings;

int ans();

int main(void) {
  cin >> N >> A >> B >> C;
  for (int i = 0; i < N; i++) {
    int tmp;
    cin >> tmp;
    toppings.push(tmp);
  }

  cout << ans();
}

int ans() {
  int max_result = 0;
  int kcal, pay;
  kcal = C;
  pay = A;


  // 도우의 열량이 매우 높고 가격은 매우 싸고 
  // 토핑의 열량이 매우 낮고 토핑의 가격이 매우 비쌀수 있음 
  max_result=kcal/pay;

  while (!toppings.empty()) {
    // 토핑 하나를 추가하고
    pay+=B;

    // 열량에 토핑 하나만큼 더함
    kcal+=toppings.top();

    // 토핑을 선택하는것이 기존의 최대열량값과 비교
    max_result=max(max_result,kcal/pay);

    toppings.pop();
  }

  return max_result;
}