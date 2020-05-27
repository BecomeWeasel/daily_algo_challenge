#include <stdio.h>
#include <stdlib.h>

#define NUMOFDWARFS 9
#define SUMOFHEIGHTS 100

int comp(const void *elem1, const void *elem2)
{
  int f = *((int *)elem1);
  int s = *((int *)elem2);
  if (f > s)
    return 1;
  if (f < s)
    return -1;
  return 0;
}

int main(void)
{
  int *heights = (int *)malloc(sizeof(int) * NUMOFDWARFS);
  int total = 0;

  int target_dwarf1 = 0;
  int target_dwarf2 = 0;

  for (int i = 0; i < NUMOFDWARFS; i++)
  {
    scanf("%d", &heights[i]);
    total += heights[i];
  }

  // printf("scanf complete\n");
  qsort(heights, NUMOFDWARFS, sizeof(int), comp);

  for (int m = 0; m < NUMOFDWARFS; m++)
  {
    for (int n = 0; n < NUMOFDWARFS; n++)
    {
      if (total - (heights[m] + heights[n]) == SUMOFHEIGHTS)
      {
        // printf("current m : %d n: %d \n", m, n);
        target_dwarf1=m;
        target_dwarf2=n;
        // printf("target dwarf1 : %d, target dwarf 2 : %d",m,n);
        for (int i = 0; i < NUMOFDWARFS; i++)
        {
          if (i == target_dwarf1 || i == target_dwarf2)
            continue;
          else
            printf("%d\n", heights[i]);
        }
        return 0;
      }
    }
  }
}
