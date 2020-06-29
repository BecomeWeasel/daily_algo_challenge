#include <iostream>
#include <vector>

using namespace std;

int N, M, K;
int remain_g, remain_b, team_count;

int ans();

int main(void) {
  cin >> N >> M >> K;
  team_count = 0;
  cout << ans();
}

int ans() {
  remain_g = N;
  remain_b = M;
  while (remain_g >= 2 && remain_b >= 1) {
    remain_g -= 2;
    remain_b -= 1;
    team_count++;
  }

  while (K > 0) {
    if (remain_g > 0) {
      remain_g--;
      K--;
    }
    else if(remain_b>0){
      remain_b--;
      K--;
    } else{
      remain_g+=2;
      remain_b+=1;
      team_count-=1;
    }
  }

  return team_count;
}