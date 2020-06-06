#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ans(int);

int main(void){
  int num;
  while(1){
    scanf("%d",&num);
    if(num==0) return 0;
    printf("%d\n",ans(num));
  }
}

int ans(int num){
  int* array=(int*)malloc(sizeof(int)*2*num+1);
  for(int i=1;i<num*2+1;i++){
    array[i]=1;
  }
  array[1]=0;

  for(int i=2;i<num*2;i++){
    if(array[i]==0) continue;


    for(int j=i+i;j<num*2+1;j+=i){
      array[j]=0;
    }
  }
  int cnt=0;
  for(int j=num+1;j<num*2+1;j++){
    // printf("current j is %d v : %d\n",j,array[j]);
    if(array[j]!=0) {
      // printf("prime : %d\n",j);
      cnt++;}
    
  }
  free(array);
  return cnt;

}