from collections import defaultdict
def solution(triangle):
    h=len(triangle)
    dp=[defaultdict(int) for _ in range(h)]
    
    dp[0][0]=triangle[0][0]
    
    for i in range(1,h):
        for j in range(len(triangle[i])):
            # 왼쪽 끝
            if j==0:
                dp[i][0]=dp[i-1][0]+triangle[i][0]
            # 오른쪽 끝
            elif j==len(triangle[i])-1:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            # 나머지는 왼쪽 위 혹은 오른쪽 위에서 내려옴
            else:
                dp[i][j]=triangle[i][j]+max(dp[i-1][j-1],dp[i-1][j]) 
    return max(dp[h-1].values())