#include <math.h>
#include <stdio.h>

void ans(int);

int sum(int);

int main(void)
{
  int X;
  scanf("%d", &X);
  ans(X);
}

int sum(int n)
{
  int sum = 0;
  for (int i = 1; i <= n; i++)
  {
    sum += i;
  }
  return sum;
}

void ans(int X)
{
  int tmp = (int)sqrt(2 * X);
  int n;
  if (sum(tmp) < X && X < sum(tmp + 1))
  {
    n = tmp;
  }
  else
  {
    n = tmp -1 ;
  }

  if ((n + 1) % 2 == 0) // even step
  {
    printf("%d/%d", X - ((n + 1) * n) / 2, n + 2 - (X - ((n + 1) * n) / 2));
  }
  else // odd steop
  {
    printf("%d/%d", n + 2 - (X - ((n + 1) * n) / 2), X - ((n + 1) * n) / 2);
  }
}