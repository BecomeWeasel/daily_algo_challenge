#include <stdio.h>
#include <stdlib.h>

#define NUM_MAX 1000000

int comp(const void *elem1, const void *elem2)
{
  int f = *((int *)elem1);
  int s = *((int *)elem2);
  if (f > s)
    return 1;
  if (f < s)
    return -1;
  return 0;
}

int main(void)
{
  int num_row;
  scanf("%d", &num_row);

  int *array = (int *)malloc(sizeof(int) * num_row);

  for (int i = 0; i < num_row; ++i)
  {
    scanf("%d",&array[i]);
  }

  qsort(array,num_row,sizeof(int),comp);

  for(int i=0;i<num_row;++i){
    printf("%d\n",array[i]);
  }
}