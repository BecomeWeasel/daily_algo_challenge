#include <iostream>

using namespace std;

#define N_MAX 1001
#define SK 1
#define CY 2

int Result[N_MAX] = {-1};
int N;

void ans();

int main(void) {
  cin >> N;
  ans();
}

void ans() {
  fill(Result, Result + N_MAX, -1);
  Result[1] = 1;
  Result[2] = 2;
  Result[3] = 1;

  // n개의 돌이 있을때
  // SK와 CY가 어떤 플레이를 하건 답은 한개 정해져있음.

  // N개의 돌이 있을때 SK가 1개, CY가 1개를 가져가면
  // SK의 순서이고 그때 결과는 N-2개의 돌의 결과와 같아짐 
  
  for (int i = 4; i <= N; i++) {
    Result[i] = Result[i - 2];
  }
  cout << ((Result[N] == 1) ? "SK" : "CY");
}