#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define FLOOR_MAX 1000001

int F,G,S,U,D;
int answer;
vector<bool>visited(FLOOR_MAX,false);

void ans();

void bfs(queue<pair<int,int>>);

int main(void){
  
  cin>>F>>S>>G>>U>>D;
  ans();
}

void ans(){
  answer=-1;
  queue<pair<int,int>> q;
  q.push(make_pair(S,0));
  visited[S]=true;

  bfs(q);
  if(answer!=-1) cout<<answer;
  else cout<<"use the stairs";
}

void bfs(queue<pair<int,int>>q){
  while(!q.empty()){
    pair<int,int> front=q.front();
    q.pop();
    int floor=front.first;
    int cnt=front.second;
    // cout<< "current floor ans cout is "<<floor<<" "<<cnt<<endl;
    
    if(floor==G){
      answer=cnt;
    }
    
    if(floor+U<=F&&!visited[floor+U]){
      q.push(make_pair(floor+U,cnt+1));
      visited[floor+U]=true;
    }
    if(floor-D>0&&!visited[floor-D]){
      q.push(make_pair(floor-D,cnt+1));
      visited[floor-D]=true;
    }
  }
}