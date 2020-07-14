#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>

using namespace std;

#define NMAX 500000
vector<int> stick(NMAX);
int N;
int ans();

int split(int, int);

int stick_sum(int,int);

int main(void) {
  cin>>N;
  for(int i=0;i<N;i++){
    cin>>stick[i];
  }
  cout<<ans();
}

int ans(){
  sort(stick.begin(),stick.begin()+N);
  int result=split(0,N-1);
  return result;
}

int split(int p,int q){
  if(p==q){
    return stick[p];
  }

  if(abs(p-q)==1){
    return stick[p]*stick[q];
  }

  int middle=(p+q)/2;


  int front=stick_sum(p,middle);
  int rear=stick_sum(middle+1,q);

  return split(p,middle)+split(middle+1,q)+front*rear;
}

int stick_sum(int start,int dest){
  int sum=0;
  for(int i=start;i<=dest;i++){
    sum+=stick[i];
  }
  return sum;
}
