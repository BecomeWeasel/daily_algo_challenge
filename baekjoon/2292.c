#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int ans(int);

int main(void)
{
  int target;
  scanf("%d", &target);
  printf("%d", ans(target));
}

int ans(int target)
{
  int n = 0;
  if(target==1){
    return 1;
  }
  int condition[2] = {2, 7};
  while (++n)
  {
    // printf("current n is %d \n", n);
    if (target >= condition[0] && target <= condition[1])
    {
      // printf("matching condition is %d %d \n", condition[0], condition[1]);
      break;
    }
    else
    {
      condition[0] += 6 * n;
      condition[1] += 6 * n + 6;
    }
    // printf("modified condition is %d %d\n", condition[0], condition[1]);
  }
  return n + 1;
}