#include <vector>
#include <iostream>

using namespace std;

int R,change_count;
int change[6]={500,100,50,10,5,1};

int ans();

int main(void){
  int num;
  cin>>num;

  R=1000-num;
  change_count=0;

  cout<<ans();
  
}

int ans(){
  for(int i=0;i<6;i++){
    while(R>=change[i]){
      R-=change[i];
      change_count++;
    }
  }
  return change_count;
}