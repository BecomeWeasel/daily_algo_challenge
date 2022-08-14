from sys import stdin, exit, setrecursionlimit

setrecursionlimit(10**9)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


N, M = map(int, stdin.readline().split())

board = []

for _ in range(N):
    line = stdin.readline().strip()

    board.append(list(map(str, line)))

visit = [[[[False for _ in range(10)] for _ in range(4)] for _ in range(M)] for _ in range(N)]

dp = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]

check = [[False for _ in range(M)] for _ in range(N)]


def sol(y, x, direction):
    global dp, check

    # if board[y][x]=='H':
    #     return 1

    # if not (0<=y<N and 0<=x<M):
    #     return 1

    if min(dp[y][x]) > 0:
        return max(dp[y][x])

    if check[y][x]:
        print(-1)
        exit()

    # if visit[y][x]
    check[y][x] = True

    step = int(board[y][x])

    for k in range(4):
        ny, nx = y + dy[k] * step, x + dx[k] * step

        if not (0 <= ny < N and 0 <= nx < M) or board[ny][nx] == "H":
            dp[y][x][k] = max(dp[y][x][k], 1)
            continue

        # if visit[ny][nx][k][step]:
        # print(-1)
        # exit()

        # visit[ny][nx][k][step]=True

        dp[y][x][k] = max(dp[y][x][k], sol(ny, nx, k) + 1)

    return max(dp[y][x])


print(sol(0, 0, 0))
