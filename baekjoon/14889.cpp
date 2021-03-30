#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int people_num;
int total_sum;
int MIN = 1000000000;
vector<vector<int> > merit;

int ans();

void dfs(int, int, int, int, vector<int>);

int total_merit_gap(vector<int>);

int main(void) {
  total_sum = 0;
  cin >> people_num;
  for (int i = 0; i < people_num; i++) {
    vector<int> row(people_num);
    for (int j = 0; j < people_num; j++) {
      int tmp;
      cin >> tmp;
      row[j]=tmp;
      total_sum += tmp;
    }
    merit.push_back(row);
  }
  cout << ans();
}

int ans() {
  vector<int> peoples;
  dfs(0, 0, 0, 0, peoples);
  return MIN;
}

void dfs(int target, int cur_people_num, int sum, int depth, vector<int> s) {
  if(target>people_num) return;
  if (cur_people_num == people_num/2) {
    sum = total_merit_gap(s);
    MIN = min(sum, MIN);
  }
  if (depth == people_num) return;
  s.push_back(target + 1);
  dfs(target + 1, cur_people_num + 1, depth + 1, sum, s);
  s.pop_back();

  dfs(target + 1, cur_people_num , depth + 1, sum, s);
}

int total_merit_gap(vector<int> v) {
  // stack 에 잇는 것들 다 빼면서 total sum에서 그만큼 빼주기
  int selected_sum = 0;
  int unselected_sum=0;

  // 총 계산 회수는 (people_num/2)*(people_num/2-1)회
  for (int i = 0; i < people_num / 2; i++) {
    for (int j = 0; j < people_num / 2; j++) {
      selected_sum += merit[v[i]-1][v[j]-1];
    }
  }
  vector<int> unselected;
  for(int h=1;h<=people_num;h++){
    if(!count(v.begin(),v.end(),h)) unselected.push_back(h);
  }
  for (int i = 0; i < people_num / 2; i++) {
    for (int j = 0; j < people_num / 2; j++) {
      unselected_sum += merit[unselected[i]-1][unselected[j]-1];
    }
  }

  return abs(unselected_sum - selected_sum);
}