#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_STUENDT 1000

int main(void)
{
  int num_test;

  scanf("%d", &num_test);
  for (int i = 0; i < num_test; i++)
  {
    int sum = 0;
    double avg = .0;
    int num_student = 0;

    scanf("%d", &num_student);
    int *scores = (int *)malloc(sizeof(int) * num_student);

    for (int j = 0; j < num_student; j++)
    {
      scanf("%d", &scores[j]);
      sum += scores[j];
      // printf("%d\n", sum);
    }
    avg = (double)sum / num_student;

    int cnt=0;
    for(int k=0;k<num_student;k++){
      if(scores[k]>avg) cnt++;
    }
    printf("%.3f%%\n",(double)cnt/num_student*100);
  }
}