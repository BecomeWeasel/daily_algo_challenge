#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<long long> fibo(90);

long long ans (long long);

int main(void){
  long long num;
  cin>>num;
  cout<<ans(num);
  return 0;

}

long long ans(long long num){
  fibo[0]=0;
  fibo[1]=1;
  for(int i=2;i<=num;i++){
    fibo[i]=fibo[i-1]+fibo[i-2];
  }

  return fibo[num];
}


