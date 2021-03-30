#include <iostream>

using namespace std;

int ans();

int L, P, V;

int main(void) {
  int i = 1;
  while (true) {
    cin >> L >> P >> V;
    if (L * P * V == 0) break;
    cout << "Case " << i++ << ": " << ans() << '\n';
  }
}

int ans() {
  int i = (V/P*P)+1;
  int cnt = V/P*L;
  int conseq_night=V-V/P*P>L?L:V-V/P*P;
  // int conseq_night=V%P>L?L:V%P;

  
  return cnt+conseq_night;
}