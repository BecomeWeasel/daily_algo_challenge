#include <iostream>
#include <vector>


using namespace std;

vector<int> tile_case(1000001);

int ans(int);

int main(void){
  int num;
  cin>>num;
  cout<<ans(num);
  return 0;
}

int ans(int num){
  tile_case[0]=0;
  tile_case[1]=1;
  tile_case[2]=2;
  for(int i=3;i<=num;i++){
    tile_case[i]=tile_case[i-1]+tile_case[i-2];
    tile_case[i]%=15746;
  }
  return tile_case[num];
}