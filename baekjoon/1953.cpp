#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define N_MAX 101

int N;
bool hate[N_MAX][N_MAX];

void ans();

int main(void) {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    int connection_num;
    int target;
    cin >> connection_num;
    for (int j = 0; j < connection_num; j++) {
      cin >> target;
      hate[i][target] = hate[target][i] = true;
    }
  }
  ans();
}

void ans() {
  vector<int> blue;
  vector<int> white;

  // 초기 값 1은 청팀으로
  blue.push_back(1);

  for (int i = 2; i <= N; i++) {
    int blue_size = blue.size();
    int white_size = white.size();

    bool flag = true;
    for (int j = 0; j < blue_size; j++) {
      if (hate[blue[j]][i] == true) flag = false;
    }

    if (flag)
      blue.push_back(i);
    else
      white.push_back(i);
  }

  // 청,백팀  출력
  cout << blue.size() << '\n';
  for (int i = 0; i < blue.size(); i++) {
    cout << blue[i] << " ";
  }
  cout << '\n';

  cout << white.size() << '\n';
  for (int i = 0; i < white.size(); i++) {
    cout << white[i] << " ";
  }
}