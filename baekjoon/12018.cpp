#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define COURSE_MAX 101

vector<vector<int>> mile(COURSE_MAX);

int n, m;

int ans();

int main(void) {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    int p, l;
    cin >> p >> l;

    // mile[i][0]에는 정원
    mile[i].push_back(l);

    for (int j = 1; j <= p; j++) {
      int tmp;
      cin >> tmp;

      mile[i].push_back(tmp);
    }

    // 실제 신청한 사람 마일리지 정렬
    // 감소하는 순서대로 정렬
    sort(mile[i].begin() + 1, mile[i].end(), greater<int>());
  }

  cout << ans();
}

int ans() {
  int course_cnt = 0;
  priority_queue<int, vector<int>, greater<int>> mile_pq;

  for (int i = 1; i <= n; i++) {
    /*
    for (int h = 1; h <= mile[i].size() - 1; h++) {
      cout << mile[i][h] << " ";
    }
    cout << "L is : " << mile[i][0] << " size is :" << mile[i].size() - 1
         << endl;

         */




    // 신청한 사람보다 정원이 많으면 1 마일만 넣어도 당첨
    if (mile[i][0] > mile[i].size() - 1) {
      mile_pq.push(1);
    }
    // 신청한 사람이 정원과 같거나 더 많다면
    // 정원의 끝(mile[i][0])에 해당하는 등수의 마일리지만큼
    // 신청하면 같을때 우선순위가 주어지니 신청가능
    else {
      mile_pq.push(mile[i][mile[i][0]]);
    }
  }

  // 마일리지가 낮은 순서부터 마일리지에서 차감하고
  // 과목을 신청함
  while (m > 0) {
    int front = mile_pq.top();
    mile_pq.pop();

    if (m - front >= 0) {
      m -= front;
      course_cnt++;
    } else
      break;
  }

  return course_cnt;
}