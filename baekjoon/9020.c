#include <stdio.h>
#include <stdlib.h>

int arr[10001];

void ans(int);

int main(void)
{
  int test_num;
  scanf("%d", &test_num);

  for (int i = 2; i < 10000; i++)
  {
    arr[i] = 1;
  }

  for (int i = 2; i < 10000; i++)
  {
    if (arr[i] == 0)
      continue;

    for (int j = i + i; j < 10000; j += i)
    {
      arr[j] = 0;
    }

    // non-prime 거르기
  }

  while (test_num--)
  {
    int num;
    scanf("%d", &num);
    ans(num);
  }
  return 0;
}

void ans(int input)
{
  int max1, max2;
  max1 = max2 = -1;

  for (int i = input / 2; i > 1; i--)
  {
    for (int j = input / 2 ; j < input; j++)
    {
      if (arr[i] != 0 && arr[j] != 0 && i + j == input)
      {
        max1 = i;
        max2 = j;
        printf("%d %d\n", max1, max2);
        return ;
      }
    }
  }
}