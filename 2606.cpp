#include <vector>
#include <iostream>

using namespace std;

#define COM_MAX 101
vector<vector<bool>> connection(COM_MAX,vector<bool>(COM_MAX,false));
vector<bool>visited(COM_MAX,false);

int com_num,pair_num,size;

int ans();

void dfs(int ,int);

int main(void){
  cin>>com_num>>pair_num;
  for(int i=0;i<pair_num;i++){
    int src,dest;
    cin>>src>>dest;
    connection[src][dest]=true;
    connection[dest][src]=true;
  }
  cout<<ans();
}

int ans(){
  size=0;
  visited[1]=true;
  dfs(1,1);
  return size;
}

void dfs(int src,int dest){
  for(int i=1;i<=com_num;i++){
    if(connection[dest][i]&&!visited[i]){
      visited[i]=true;
      size++;
      dfs(dest,i);
    }
  }
}
