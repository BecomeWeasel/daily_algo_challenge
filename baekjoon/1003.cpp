#include <vector>
#include <iostream>

using namespace std;

void ans(int);

vector<int> f0(41);
vector<int> f1(41);


int main(void){
  int test_num;
  cin>>test_num;
  while(test_num--){
    int num;
    cin>>num;
    ans(num);
  }
}


void ans(int num){
  f0[0]=1;
  f1[0]=0;

  f0[1]=0;
  f1[1]=1;

  for(int i=2;i<=num;i++){
    f0[i]=f0[i-1]+f0[i-2];
    f1[i]=f1[i-1]+f1[i-2];
  }


  cout<<f0[num]<<" "<<f1[num]<<'\n';
}