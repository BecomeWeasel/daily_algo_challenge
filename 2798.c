#include <stdio.h>
#include <stdlib.h>

int ans(int, int, int*);

int main(void) {
  int num_card, sum;
  int* cards;
  scanf("%d %d", &num_card, &sum);
  cards = (int*)malloc(sizeof(int) * num_card);
  for (int i = 0; i < num_card; i++) {
    scanf("%d", &cards[i]);
  }
  printf("%d", ans(num_card, sum, cards));
}

int ans(int num_card, int sum, int* cards) {
  int max = 0;
  for (int i = 0; i < num_card; i++) {
    for (int j = 0; j < num_card; j++) {
      if (j == i) continue;
      for (int k = 0; k < num_card; k++) {
        if (k == j || k == i) {
          continue;
        }
        if (cards[i] + cards[j] + cards[k] <= sum &&
            cards[i] + cards[j] + cards[k] > max) {
          max = cards[i] + cards[j] + cards[k];
        }
      }
    }
  }

  return max;
}