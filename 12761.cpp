#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define BRDIGE_SIZE_MAX 100001

vector<bool> visited(BRDIGE_SIZE_MAX,false);

int N,M,A,B;

int ans();

int bfs(queue<pair<int,int>>);

int main(void){
  cin>>A>>B>>N>>M;
  cout<<ans();
}

int ans(){
  queue<pair<int,int>> q;

  q.push(make_pair(N,0));
  visited[N]=true;
  return bfs(q);
}

int bfs(queue<pair<int,int>> q){
  while(!q.empty()){
    pair<int,int> front=q.front();
    q.pop();

    if(front.first==M){
      return front.second;
    }

    if(front.first-1>=0&&!visited[front.first-1]){
      q.push(make_pair(front.first-1,front.second+1));
      visited[front.first-1]=true;
    }
    if(front.first+1<BRDIGE_SIZE_MAX&&!visited[front.first+1]){
      q.push(make_pair(front.first+1,front.second+1));
      visited[front.first+1]=true;
    }

    if(front.first+A<BRDIGE_SIZE_MAX&&!visited[front.first+A]){
      q.push(make_pair(front.first+A,front.second+1));
      visited[front.first+A]=true;
    }
    if(front.first-A>=0&&!visited[front.first-A]){
      q.push(make_pair(front.first-A,front.second+1));
      visited[front.first-A]=true;
    }

    if(front.first+B<BRDIGE_SIZE_MAX&&!visited[front.first+B]){
      q.push(make_pair(front.first+B,front.second+1));
      visited[front.first+B]=true;
    }
    if(front.first-B>=0&&!visited[front.first-B]){
      q.push(make_pair(front.first-B,front.second+1));
      visited[front.first-B]=true;
    }

    if(front.first*A<BRDIGE_SIZE_MAX&&!visited[front.first*A]){
      q.push(make_pair(front.first*A,front.second+1));
      visited[front.first*A]=true;
    }
    if(front.first*B<BRDIGE_SIZE_MAX&&!visited[front.first*B]){
      q.push(make_pair(front.first*B,front.second+1));
      visited[front.first*B]=true;
    }
  }

  return -1;
}