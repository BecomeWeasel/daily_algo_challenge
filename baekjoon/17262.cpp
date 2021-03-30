#include <iostream>
#include <vector>


using namespace std;

#define NMAX 100000

vector<pair<int,int>> times(NMAX);
int N;

int ans();

int main(void){
  cin>>N;
  cout<<ans();
}

int ans(){
  int shortest_end=100000;
  int latest_start=0;

  for(int i=0;i<N;i++){
    int start,end;
    cin>>start>>end;

    shortest_end=min(shortest_end,end);
    latest_start=max(latest_start,start);

    times[i]=make_pair(start,end);

  }

  if(shortest_end>=latest_start) return 0;
  else return latest_start-shortest_end;
}