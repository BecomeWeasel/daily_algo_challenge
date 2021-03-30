#include <iostream>
#include <vector>

using namespace std;

vector<long long> pa(101);

long long ans(int);

int main(void) {
  int test_num;
  cin >> test_num;
  while (test_num--) {
    int num;
    cin>>num;
    cout << ans(num)<<'\n';
  }
  return 0;
}

long long ans(int num) {
  pa[1] = 1;
  pa[2] = 1;
  pa[3] = 1;
  pa[4] = 2;
  pa[5] = 2;
  for (int i = 6; i <= num; i++) {
    pa[i] = pa[i - 1] + pa[i - 5];
  }
  return pa[num];
}
