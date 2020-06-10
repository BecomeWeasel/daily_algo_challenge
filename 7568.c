#include <stdio.h>
#include <stdlib.h>

struct body {
  int weight;
  int height;
  int pos;
};

void ans(struct body*, int);

int main(void) {
  int num;
  scanf("%d", &num);
  struct body* ptr = (struct body*)malloc(sizeof(struct body) * num);
  for (int i = 0; i < num; ++i) {
    scanf("%d %d", &ptr[i].weight, &ptr[i].height);
  }
  ans(ptr, num);
  return 0;
}

void ans(struct body* bodyptr, int num) {
  for (int i = 0; i < num; i++) {
    int cnt = 0;
    for (int j = 0; j < num; j++) {
      if (i == j) continue;
      if (bodyptr[i].height < bodyptr[j].height &&
          bodyptr[i].weight < bodyptr[j].weight) {
        cnt++;
      }
    }
    i != num - 1 ? printf("%d ", cnt + 1) : printf("%d", cnt + 1);
  }
}