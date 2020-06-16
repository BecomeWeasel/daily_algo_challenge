#include <iostream>
#include <vector>

using namespace std;

int dp[1001][3];
vector<vector<int> > costs;
int house_num;

int ans();

int main(void) {
  cin >> house_num;
  for (int i = 0; i < house_num; i++) {
    vector<int> rgb;
    int r, g, b;
    cin >> r >> g >> b;
    rgb.push_back(r);
    rgb.push_back(g);
    rgb.push_back(b);

    costs.push_back(rgb);
  }
  cout << ans();

  return 0;
}

int ans() {

  for (int i = 1; i <= house_num; i++) {
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+costs[i-1][0];
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+costs[i-1][1];
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+costs[i-1][2];
  }
  return min(min(dp[house_num][0], dp[house_num][1]), dp[house_num][2]);
}