#include <stdio.h>
#include <stdlib.h>

int ans(int *, int);

int main(void)
{
  int num;
  int *array;
  scanf("%d", &num);

  array = (int *)malloc(sizeof(int) * num);
  int i = 0;
  while (i < num)
  {
    scanf("%d", &array[i++]);
  }
  printf("%d", ans(array, num));
}

int ans(int *array, int num)
{
  int cnt = 0;

  for (int i = 0; i < num; i++)
  {
    // printf("%d\n",i);
    if (array[i] == 1)
    {
      continue;
    }
    for (int j = 2; j <= array[i]; j++)
    {
      // printf("cmp : %d,%d\n",j,array[i]);
      if (j == array[i])
      {
        cnt++;
        break;
      }
      if (array[i] % j == 0)
        break;
    }
  }
  return cnt;
}