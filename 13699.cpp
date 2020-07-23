// #include <time.h>

#include <iostream>
#include <vector>

using namespace std;

#define N_MAX 36

int N;
// clock_t t_start, t_end;

vector<long long> t(N_MAX, -1);

long long ans(int);

int main(void) {
  // t_start = clock();
  // double result;
  cin >> N;
  t[0] = 1;
  t[1] = 1;

  cout << ans(N) << endl;
  // t_end = clock();

  // cout << (double)(t_end - t_start);
}

long long ans(int idx) {
  long long ret = 0;
  if (t[idx] != -1)
    return t[idx];
  else {
    for (int k = 0; k <= idx - 1; k++) {
      ret += ans(k) * ans(idx - 1 - k);
    }
    t[idx] = ret;
  }
  return ret;
}