#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
#define MAX 100

int N;
bool is_printed=false;
vector<int> up(MAX, 0);
vector<int> down(MAX, 0);

void ans();

void dfs(int, int, vector<int>);

void print(vector<int>);

int main(void) {
  cin >> N;
  for (int i = 0; i < MAX; i++) {
    up[i] = i + 1;
  }
  for (int i = 0; i < N; i++) {
    int tmp;
    cin >> tmp;
    down[i] = tmp;
  }
  ans();
}

void ans() {
  for (int i = N; i > 0; i--) {
    if(is_printed) return;
    // 길이가 최대인것을 찾아야하니 끝에서부터
    for (int j = 0; j < N; j++) {
      if(is_printed) return;
      vector<int> selected;
      selected.push_back(j);
      dfs(j, i, selected);
    }
  }
}

void dfs(int src, int target_size, vector<int> v_selected) {
  if(is_printed) return;
  if (v_selected.size() == target_size&&!is_printed) {
    bool flag = true;
    vector<int> v_down;
    for (int i = 0; i < target_size; i++) {
      v_down.push_back(down[v_selected[i]]);
    }
    sort(v_down.begin(), v_down.end());
    for (int i = 0; i < target_size; i++) {
      if (up[v_selected[i]] != v_down[i]) {
        flag = false;
        break;
      }
    }

    if (flag) {
      print(v_selected);
      is_printed=true;
    }

  } else {
    for (int i = src + 1; i < N; i++) {
      v_selected.push_back(i);
      dfs(i, target_size, v_selected);
      v_selected.pop_back();
    }
  }
}

void print(vector<int> v_selected) {
  cout << v_selected.size() << '\n';
  for (int i = 0; i < v_selected.size(); i++) {
    cout << up[v_selected[i]] << '\n';
  }
}