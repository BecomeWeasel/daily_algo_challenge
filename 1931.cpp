#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX 100000
int cnt, N;
vector<pair<int, int>> meet_time(MAX);

bool compare(const pair<int, int>& a, const pair<int, int>& b) {
  return (a.second < b.second);
}

int ans();

int main(void) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    int start, finish;
    cin >> start >> finish;
    meet_time[i] = make_pair(start, finish);
  }
  cout << ans();
}

int ans() {
  sort(meet_time.begin(), meet_time.begin() + N);
  // cout << endl;
  // cout << endl;
  // cout << endl;

  // for (int i = 0; i < N; i++) {
  //   cout << meet_time[i].first << " " << meet_time[i].second;
  //   cout << endl;
  // }
  // cout << endl;
  // cout << endl;
  // cout << endl;
  // cout << endl;
  // cout << endl;
  sort(meet_time.begin(), meet_time.begin() + N, compare);
  // for (int i = 0; i < N; i++) {
  //   cout << meet_time[i].first << " " << meet_time[i].second;
  //   cout << endl;
  // }

  int min = meet_time[0].second;
  cnt++;
  for (int i = 1; i < N; i++) {
    if (meet_time[i].first >= min) {
      min = meet_time[i].second;
      cnt++;
    }
  }
  return cnt;
}