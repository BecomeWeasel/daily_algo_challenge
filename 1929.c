#include <stdio.h>
#include <stdlib.h>

void ans (int,int);

#define MAX 1000001
int array[MAX]={0};

int main(void){
  

  int num1,num2;
  scanf("%d %d",&num1,&num2);


  for(int i=2;i<MAX;++i){
    array[i]=1;
  }
  ans(num1,num2);

}

void ans(int num1,int num2){
  // printf("pass24\n");
  for(int i=2;i<num2;i++){
    // printf("current value : %d\n",i);
    if(array[i]==0)
      continue;
     
     for(int j=i*2;j<MAX;j+=i){
       array[j]=0;
     }
  }
  // printf("pass31\n");

  for(int i=num1;i<=num2;i++){
    if(array[i]!=0)
      printf("%d\n",i);
  }
}