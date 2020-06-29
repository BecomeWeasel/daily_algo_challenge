#include <iostream>
#include <vector>
using namespace std;

#define MAX 1000001

int pass;
int N;
vector<int> meet_case(MAX);

int ans();

int main(void) {
  int test_num;
  cin >> test_num;
  while (test_num--) {
    cin >> N;
    for (int i = 0; i < N; i++) {
      int paper, meet;
      cin >> paper >> meet;
      meet_case[paper] = meet;
    }
    cout << ans();
    cout << '\n';
  }
}

int ans() {
  pass = 1;
  int tmp_rank=meet_case[1];

 // 기존 코드 사용하면 TLE 위험 있음
  // for (int i = 1; i <= N; i++) {
  //   for (int j = i; j > 0; j--) {
  //     if (meet_case[i] > meet_case[j]) {
  //       pass--;
  //       break;
  //     }
  //   }
  // }

  // 기존에 합격한 사람보다 면접순위가 더 높으면 그사람은
  // 서류에서 밀리더라도 (i가 1에서부터 쭉 증가하니 )
  // 최종합격 (면접 순위가 밀리지 않으니)
   for (int i = 2; i <= N; i++) {
    if(meet_case[i]<tmp_rank) {
      pass++;
      tmp_rank=meet_case[i];
    }
  }

  return pass;
}