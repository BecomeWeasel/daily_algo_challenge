from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    benefit = {}
    benefit[0] = [0 for _ in range(M)]
    for i in range(1, N + 1):
        s = list(map(int, stdin.readline().split()))

        benefit[i] = s[1:]
    # 1<=N<=300 , 1<=M<=20

    # 많이 투자할수록 이익이 많이 생김

    # 만약에 특정기업에 단순 투자한다 , 안한다면 비트마스킹으로 바로 풀 수 있을거같은데................................
    # 이건 특정기업에 0~N만원까지 투자할 수 있어서 골치아픈데

    # 어쨋든 모든 계산은 해봐야함.......
    # 모두 계산하면 , O(M*N*N)=O(20*300*300)

    dp = [[0 for _ in range(M)] for _ in range(N + 1)]

    # i_p_r[company][amount] = company번째 투자를 한 뒤에 투자금액이 amount일때, 그 기업에 얼마를 투자했는지 기록

    invest_per_company = {}
    invest_per_company[0] = {}

    for money in range(N + 1):
        dp[money][0] += benefit[money][0]
        # invest_per_company[0][money]=benefit[money][0] <<<<<<<<<<<< 이부분에서 대형실수
        invest_per_company[0][money] = money

    for company in range(1, M):
        invest_per_company[company] = {}
        for money in range(N + 1):
            # 이거 어렵게 생각하지말고, 5번 회사에 투자 얼마할지 결정한다고 해보자.
            # 그럼 사실 초기는 5번 회사에 아무것도 투자안함(0원)
            # 그러면 1,2,3,4번에 money만큼 투자한거랑 이익이 같음.
            # 그러면 dp[money][4]=dp[money][5] 인 상태에서 ,
            # 1원씩 늘려서 투자해보자는 거임
            # dp[money+1][5] vs dp[money][4] + 5번에 1원 투자할때 이익
            for cost in range(N - money + 1):

                if dp[cost + money][company] < dp[money][company - 1] + benefit[cost][company]:
                    dp[cost + money][company] = dp[money][company - 1] + benefit[cost][company]

                    invest_per_company[company][cost + money] = cost

    # print(invest_per_company)

    print(dp[N][M - 1])
    backtrace_money, company = N, M - 1
    answer = []
    while company >= 0:
        answer.append(invest_per_company[company][backtrace_money])
        backtrace_money -= invest_per_company[company][backtrace_money]
        company -= 1

    print(" ".join(map(str, reversed(answer))))


# print(sol())
sol()
