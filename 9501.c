#include <stdio.h>
#include <stdlib.h>


int main(void){
  int num_test_case;
  scanf("%d",&num_test_case);


  for(int i=0;i<num_test_case;i++){
    int num_spaceship=0;
    int distance=0;
    int num_success=0;
    scanf("%d %d",&num_spaceship,&distance);

    double speed[1000];
    double capacity[1000];
    double efficiency[1000];

    for(int j=0;j<num_spaceship;j++){
      scanf("%lf %lf %lf",&speed[j],&capacity[j],&efficiency[j]);
      if(distance/speed[j]*efficiency[j]<=capacity[j])
        num_success++;
    }
    printf("%d\n",num_success);
  }


  return 0;
}