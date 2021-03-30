#include <stdio.h>
#include <math.h>

void ans(int,int,int);

int main(void){
  int test_num;
  scanf("%d",&test_num);

  for(int i=0;i<test_num;++i){
  int H,W,N;
  scanf("%d %d %d",&H,&W,&N);
  ans(H,W,N);
  }
}

void ans (int h,int w,int n){
  int fore_num,rear_num;

  if(n%h==0){
    fore_num=h;
    rear_num=n/h;
  }else{
    fore_num=n%h;
    rear_num=n/h+1;
  }


  printf("%d\n",100*fore_num+rear_num);


}