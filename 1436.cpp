#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int ans(int);

int main(void) {
  int num;
  cin >> num;
  cout << ans(num);
}

int ans(int num) {
  int cnt = 0;
  int title_num = 1;
  while (title_num++) {
    string s = to_string(title_num);
    if (s.find("666") != string::npos) cnt++;
    if (cnt == num)
      return title_num;
    else
      continue;
  }
}
