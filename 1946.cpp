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
  pass = N;

  for (int i = 1; i <= N; i++) {
    for (int j = i; j > 0; j--) {
      if (meet_case[i] > meet_case[j]) {
        pass--;
        break;
      }
    }
  }

  return pass;
}