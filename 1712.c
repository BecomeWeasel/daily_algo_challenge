#include <stdio.h>
#include <math.h>

long ans(long, long, long);

int main(void)
{
  long A, B, C;
  scanf("%ld %ld %ld", &A, &B, &C);

  printf("%ld", ans(A, B, C));
}

long ans(long A, long B, long C)
{
  long n = 0;
  if (B >= C)
    return -1;
  else
    return A/(C-B) + 1;
  
}