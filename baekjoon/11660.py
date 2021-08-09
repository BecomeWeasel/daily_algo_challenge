from sys import stdin


def sol():
    N, M = map(int, stdin.readline().split())

    board = []

    for _ in range(N):
        board.append(list(map(int, stdin.readline().split())))

    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0:
                dp[i][0] = board[i][0]
            else:
                dp[i][j] = board[i][j] + dp[i][j - 1]
    result = ''
    for _ in range(M):
        y1, x1, y2, x2 = map(int, stdin.readline().split())
        x1,y1,x2,y2=map(lambda x:x-1,[x1,y1,x2,y2])

        # print(x1,y1,x2,y2)
        
        total=0
        for y in range(y1,y2+1):
            if x1==0:
                total+=dp[y][x2]
            else:
                total+=dp[y][x2]-dp[y][x1-1]
            # print(total)
        print(total)


sol()