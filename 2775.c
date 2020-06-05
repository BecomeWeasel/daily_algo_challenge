#include <stdio.h>
#include <math.h>

// TODO : 재귀로 풀어보기. 

int room[15][15]={0};

int cumulative_sum(int);
int ans (int,int);

int main(void){
  int test_num;
  scanf("%d",&test_num);
  while(test_num--){
    int k,n;
    scanf("%d\n%d",&k,&n);
    printf("%d\n",ans(k,n));
  }

}

int ans (int k,int n){
  if(k>0){
    int sum=0;
    for(int i=1;i<=n;i++){
      sum+=ans(k-1,i);
    }
    return sum;
  }else{
    return n;
  }
}

int cumulative_sum(int n)
{
  if (n>0)
    return n+cumulative_sum(n-1);
  else 
    return 0;
}