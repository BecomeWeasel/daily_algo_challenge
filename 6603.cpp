#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

#define MAX 13
#define lottery_num 6

int k;

vector<int>number(MAX,0);

void ans();

void dfs(int,int,vector<int>);

void print(vector<int>);

int main(void) {
  while (true) {
    cin >> k;
    if (k == 0)
      return 0;
    else {
      for(int i=0;i<k;i++){
        int tmp;
        cin>>tmp;
        number[i]=tmp;
      }
      ans();
      fill(number.begin(),number.end(),0);
      cout<<'\n';
    }
  }
}

void ans(){
  for(int i=0;i<k;i++){
    vector<int> list;
    list.push_back(i);
    dfs(i,1,list);
  }
}

void dfs(int src,int size,vector<int> v_num){
  if(size==lottery_num){
    print(v_num);
    return ;
  }

  for(int i=src+1;i<k;i++){
    v_num.push_back(i);
    dfs(i,size+1,v_num);
    v_num.pop_back();
  }
}

void print(vector<int> v_num){
  for(int i=0;i<lottery_num;i++)
    cout<<number[v_num[i]]<<" ";
  cout <<'\n';
}