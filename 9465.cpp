#include <iostream>
#include <vector>

using namespace std;

#define MAX 100000
int num;

int ans(vector<vector<int> >, int);

int main(void) {
  int test_num;
  cin >> test_num;
  while (test_num--) {
    int num;
    cin >> num;
    vector<vector<int> > card;

    for (int i = 0; i < 2; i++) {
      vector<int> row(num + 1);
      for (int i = 1; i <= num; i++) {
        int tmp;
        cin >> tmp;
        row[i] = tmp;
      }
      card.push_back(row);
    }
    cout << ans(card, num);
    cout << '\n';
  }
}

int ans(vector<vector<int> > card, int num) {
  int dp[2][num + 1];
  dp[0][0] = 0;
  dp[1][0] = 0;
  dp[0][1] = card[0][1];
  dp[1][1] = card[1][1];

  for (int i = 2; i <=num; i++) {
    dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + card[0][i];
    dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + card[1][i];
  }


  return max(dp[0][num], dp[1][num]);
}