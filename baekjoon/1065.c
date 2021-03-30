#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DIGIT 4

int ans(char *);

int main(void)
{
  char num[MAX_DIGIT];
  scanf("%s", num);
  // printf("%s", num);
  int cnt = 0;
  // printf("%lu", strlen(num));

  int num_int = atoi(num);
  // printf("%d", num_int);
  // int cnt = 0;

  printf("%d", ans(num));
}

int ans(char *char_num)
{
  int num_int = atoi(char_num);
  if (num_int < 100)
  {
    return num_int;
  }
  else if (num_int == 1000)
  {
    return ans("999");
  }
  else if (num_int == 100)
  {
    return ans("99");
  }
  else
  {
    int cnt = 0;
    while (num_int > 100)
    {
      int first = num_int/100;
      int second = (num_int-first*100)/10;
      int third = (num_int-first*100-second*10);
      // printf("num int is %d f: %d s: %d t : %d\n",num_int,first,second,third);
      if ((second - first) == (third - second)){
        cnt++;
        // printf("num int : %d\n",num_int);
      }
      num_int--;
    }

    return cnt + ans("100");
  }
}