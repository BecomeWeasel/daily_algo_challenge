#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int n;
vector<int> op;
vector<int> num;

int MIN = 1000000000;
int MAX = -1000000000;

void ans();

void dfs(int, int, int, int, int, int);

int main(void) {
  cin >> n;
  for (int i = 0; i < n; i++) {
    int tmp;
    cin >> tmp;
    num.push_back(tmp);
  }

  for (int i = 0; i < 4; i++) {
    int tmp;
    cin >> tmp;
    op.push_back(tmp);
  }

  ans();
}

void dfs(int plus, int minus, int mul, int div, int len, int output) {
  if (len == n) {
    if (output > MAX) MAX = output;
    if (output < MIN) MIN = output;
  }
  if(plus>0)
    dfs(plus-1,minus,mul,div,len+1,output+num[len]);
  if(minus>0)
    dfs(plus,minus-1,mul,div,len+1,output-num[len]);
  if(mul>0)
    dfs(plus,minus,mul-1,div,len+1,output*num[len]);
  if(div>0)
    dfs(plus,minus,mul,div-1,len+1,output/num[len]);

}

void ans(){
  dfs(op[0],op[1],op[2],op[3],1,num[0]);
  cout<<MAX<<'\n';
  cout<<MIN;
}