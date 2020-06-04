#include <stdio.h>
#include <math.h>

// TODO : 재귀로 풀어보기. 

int room[15][15]={0};

int sum(int);
int ans (int,int);
int room_initialize();

int main(void){
  room_initialize();
  int test_num;
  scanf("%d",&test_num);
  while(test_num--){
    int k,n;
    scanf("%d\n%d",&k,&n);
    printf("%d\n",ans(k,n));
  }

}

int ans (int k,int n){
  return room[k][n];
}

int room_initialize(){
  for(int j=1;j<15;j++){
    room[0][j]=j;
  }
  for(int h=1;h<15;h++){
    for(int k=1;k<15;k++){
      int room_sum=0;
      for(int p=1;p<k+1;p++){
        room_sum+=room[h-1][p];
        // printf("room sum : %d\n",room_sum);
      }
      room[h][k]=room_sum;
    }
  }

}

int sum(int n)
{
  if (n>0)
    return n+sum(n-1);
  else 
    return 0;
}