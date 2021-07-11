from sys import stdin


T=int(stdin.readline())

def sol():
    dp=[0 for _ in range(11)]

    dp[1]=1
    dp[2]=2
    dp[3]=4

    for n in range(4,11):
        dp[n]=dp[n-1]+dp[n-2]+dp[n-3]

    answer=''
    for _ in range(T):
        answer=answer+str(dp[int(stdin.readline())])+'\n'
    return answer.rstrip()

print(sol())