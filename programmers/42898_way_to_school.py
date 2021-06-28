def solution(x, y, puddles):
    answer = 0
    
    dp=[[0 for _ in range(x+1)] for _ in range(y+1)]
    dp[1][1]=1
    
    for x_,y_ in puddles:
        dp[y_][x_]=-1
        
    # top down
    def get_routes(i,j,dp,y,x,puddles):
        # 이미 계산한 값이거나 시작점이라면
        if dp[i][j]>0:
            return dp[i][j]
        # 범위를 벗어낫다면
        if (not 1<=i<=y) or (not 1<=j<=x):
            return 0
        # 웅덩이라면 패스
        if [j,i] in puddles:
            return 0
        
        dp[i][j]= get_routes(i-1,j,dp,y,x,puddles)+get_routes(i,j-1,dp,y,x,puddles)
        return dp[i][j]
        
    return get_routes(y,x,dp,y,x,puddles)%1000000007
    
    '''
    #bottom up
    for i in range(1,y+1):
        for j in range(1,x+1):
            # 웅덩이는 경로 계산 X
            if dp[i][j]==-1:
                continue
            # 웅덩이가 아니라면
            if 1<=i+1<=y and dp[i+1][j]!=-1:
                dp[i+1][j]+=dp[i][j]
            
            if 1<=j+1<=x and dp[i][j+1]!=-1:
                dp[i][j+1]+=dp[i][j]
    
    
    return dp[y][x]%1000000007
    '''