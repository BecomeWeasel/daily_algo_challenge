#include <iostream>

using namespace std;

int T;
void ans();

int main(void) {
  cin >> T;
  ans();
}

void ans() {
  int a, b, c;
  a = b = c = 0;
  int button[3] = {300, 60, 10};

  while (T >= button[0]) {
    T -= button[0];
    a++;
  }
  while (T >= button[1]) {
    T -= button[1];
    b++;
  }
  while (T >= button[2]) {
    T -= button[2];
    c++;
  }

  if (T == 0) {
    cout << a << " " << b << " " << c;
  } else {
    cout << -1;
  }
}