#include <string.h>

#include <iostream>
#include <string>

using namespace std;
#define BOARDMAX 500

// char board[BOARDMAX];
string s;

void ans();

int main(void) {
  cin >> s;
  ans();
}

void ans() {
  int i = 0;
  // cout<<s.size()<<endl;
  while (i < s.size()) {
    if (s[i] == '.')
      i++;
    else if (s[i] == 'X' && s[i + 1] == 'X' && s[i + 2] == 'X' &&
             s[i + 3] == 'X') {
      s.replace(i, 4, "AAAA");
      i += 4;
      // cout<<s<<endl;
    } else if (s[i] == 'X' && s[i + 1] == 'X') {
      
      s.replace(i, 2, "BB");
      i += 2;
      // cout<<s<<endl;
    }
    // i는 X지만 i+1은 X가 아닐때
    // 덮을수 없음
    else if (s[i + 1] != 'X') {
      cout << -1;
      return;
    }
  }
  cout << s;
}