#include <stdio.h>

int ans(int);
int main(void)
{
  int weight = 0;
  scanf("%d", &weight);

  printf("%d", ans(weight));
}

int ans(int weight_input)
{
  int five = 0;
  int three = 0;
  int weight = weight_input;

  for (five = weight / 5; five >= 0; weight += five * 5,five--)
  {
    weight -= five * 5;
    if (weight % 3 == 0)
    {
      three = weight / 3;
      return three + five;
    }
    else
      continue;
  }
  return -1;
}