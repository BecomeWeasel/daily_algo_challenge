#include <stdio.h>

#define MAX 1000000

int ans(int);

int main(void) {
  int num;
  scanf("%d", &num);
  printf("%d", ans(num));
}

int ans(int num) {
  int sum;

  int bottom = 0;
  int min = MAX;
  while (++bottom<num) {
    
    sum = 0;
    int tmp = bottom;
    while (tmp > 0) {
      sum += tmp % 10;
      tmp /= 10;
    }
    // printf("c num is %d sum is %d\n",bottom,sum);
    if (num == bottom + sum) return bottom;
  }

  return 0;
}