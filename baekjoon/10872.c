#include <stdio.h>

int ans(int);

int main(void) {
    int num;
    scanf("%d", &num);
    printf("%d", ans(num));
}

int ans(int num) {
  if (num<=1) return 1;
  else return num*ans(num-1);
}