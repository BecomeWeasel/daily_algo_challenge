#include <iostream>

using namespace std;

#define NMAX 30000
int N;

int cliff[NMAX];

int ans();

int main(void) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> cliff[i];
  }

  cout << ans();
}

int ans() {
  int max_result = -1;
  for (int i = 0; i < N; i++) {
    int target = 0;
    for (int j = i + 1; j < N; j++) {
      if
        (cliff[i] < cliff[j]) break;
      else
        target++;
    }
    max_result=max(max_result,target);
  }
  return max_result;
}
