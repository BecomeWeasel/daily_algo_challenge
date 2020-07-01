#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

#define LEN_MAX 51
#define NUM_MAX 1001

int N, M;
char dna[4] = {'A', 'C', 'G', 'T'};
vector<string> v_dna(NUM_MAX);

void ans();

int main(void) {
  cin >> N >> M;
  for (int i = 1; i <= N; i++) {
    cin >> v_dna[i];
  }
  ans();
}

void ans() {
  int diff_sum = 0;
  string dna_string("");
  for (int i = 1; i <= M; i++) {
    vector<int> dna_diff(4); 
    // 각각의 A G C T에 대해서 문자들이 얼마나 차이나는지 기록
    for (int h = 0; h < 4; h++) {
      for (int j = 1; j <= N; j++) {
        if (dna[h] != v_dna[j][i - 1]) dna_diff[h]++;
      }
    }
    // DNA 차이중에서 가장 적게 차이나는 값을 골라옴
    int min_dna_diff =
        min(min(min(dna_diff[0], dna_diff[1]), dna_diff[2]), dna_diff[3]);
    
    int min_pos=0;
    // min값을 가져오고 그 pos를 찾아야함
    for (int k = 0; k< 4; k++) {
      if (dna_diff[k] == min_dna_diff) {
        min_pos = k; 
        break;
        // 사전순으로 나와야하기때문에 하나라도 중복된 min 값이라도
        // 발견하면 break로 빠져나옴 
      }
    }
    dna_string.push_back(dna[min_pos]);
    diff_sum += min_dna_diff;
  }

  cout << dna_string << endl;
  cout << diff_sum;

}

