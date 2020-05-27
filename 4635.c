#include <stdio.h>
#include <stdlib.h>

int main(void)
{

  while (1)
  {
    int num_rows = 0;
    scanf("%d", &num_rows);
    if (num_rows < 0)
    {
      return 0;
    }

    int total_miles = 0;
    int *mile_indicator = (int *)malloc(sizeof(int) * (num_rows + 1));
    int *time_elapsed = (int *)malloc(sizeof(int) * (num_rows + 1));

    mile_indicator[0] = 0;
    time_elapsed[0] = 0;

    for (int i = 1; i < num_rows + 1; i++)
    {
      scanf("%d %d",&mile_indicator[i],&time_elapsed[i]);
      total_miles += mile_indicator[i] * (time_elapsed[i] - time_elapsed[i - 1]);
    }
    printf("%d miles\n",total_miles);
  }
}