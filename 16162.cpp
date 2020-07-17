#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 20001

int sounds[N_MAX];

int n, a, d;

int ans();

int main(void) {
  cin >> n >> a >> d;
  for (int i = 1; i <= n; i++) {
    cin >> sounds[i];
  }

  cout << ans();
}

int ans() {
  int x = 0;

  // 첫 다음항은 초항
  int next = a;


  // 공차수열은 만족하는 다음 음을 찾기
  for (int i = 1; i <= n; i++) {
    if(sounds[i]==next){
      next+=d;
      x++;
    }
  }
  return x;
}