#include <algorithm>
#include <cstring>  //memset
#include <iostream>
#include <string>

using namespace std;

const int MAX = 250 + 1;

int N;

string dp[MAX];

string bigNumAdd(string num1, string num2)

{
  long long sum = 0;

  string result;

  // 1의 자리부터 더하기 시작한다

  while (!num1.empty() || !num2.empty() || sum)

  {
    if (!num1.empty())

    {
      sum += num1.back() - '0';

      num1.pop_back();
    }

    if (!num2.empty())

    {
      sum += num2.back() - '0';

      num2.pop_back();
    }

    //다시 string 형태로 만들어 push_back

    result.push_back((sum % 10) + '0');

    sum /= 10;
  }

  // 1의 자리부터 result에 넣었으므로 뒤집어줘야한다

  reverse(result.begin(), result.end());

  return result;
}

int main(void)

{
  // 이유는 모르겠지만 0일때 1로 해야함.
  dp[0] = dp[1] = '1';

  // N일때는 N-1까지에서 2x1크기의 하나만 더 넣으면 되고
  // N-2까지에서 2x2 1개,1x2 두개로 만들수 있으니
  // dp[n]=dp[n-1]+2*dp[n-2];

  for (int n = 2; n <= 250; n++)

    dp[n] = bigNumAdd(bigNumAdd(dp[n - 2], dp[n - 2]), dp[n - 1]);

  while (~scanf("%d", &N))

  {
    cout << dp[N] << endl;
  }

  return 0;
}
