#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 11
int N;
vector<int> left_taller(MAX);

void ans();

int main(void) {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    cin >> left_taller[i];
  }
  ans();
}

void ans() {
  vector<int> line_position(MAX, -1);
  line_position[left_taller[1] + 1] = 1;
  // 1보다 큰 사람은 없으니 1의 위치는 항상 고정됨 . 
  // 예를 들어 1이 3이면 왼쪽에 자기보다 큰 3명이니 1은 무조건 4번째

  for (int i = 2; i <= N; i++) {
    int position_count = 0; // 빈 자리 중에서 왼쪽에서부터 몇번째 빈자리인지
    for (int j = 1; j <= N; j++) {
      if (position_count == left_taller[i] && line_position[j] == -1) {
        // 빈자리이고 현재 빈자리를 적절히 지나왔다면
        line_position[j] = i; 
        break;
      }
      // 빈자리를 지나침
      if (line_position[j] == -1) position_count++;
    }
  }

  for (int i = 1; i <= N; i++) {
    cout << line_position[i] << " ";
  }
}
