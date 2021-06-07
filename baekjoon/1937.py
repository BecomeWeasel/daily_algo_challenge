from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**6)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
MAX_DAY = -1

N = int(stdin.readline())

board = list()
for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]


def dfs(y, x):
    global N, board, dp

    # (y,x)에 대해서 최장기간 사는 날이 계산되어있으면
    # 다시 탐색을 할필요가 없음
    # dp의 활용
    if dp[y][x]:
        return dp[y][x]

    # (y,x)에 대해서 사는날이 계산 안되어 있으니
    # 초기값 1로 설정
    dp[y][x] = 1

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]

        if 0 <= ny < N and 0 <= nx < N:
            if board[ny][nx] > board[y][x]:
                # 내 옆칸이 나보다 대나무가 많다면
                # 내 옆칸 생존일수보다 하루는 더 살수 있음
                # 내 옆칸 생존일수에 대해서 재귀적으로 계산
                dp[y][x] = max(dfs(ny, nx) + 1, dp[y][x])
    
    # 이제는 (y,x)에 대해서 최장기간 사는날이 구해져있음.
    # 다음에 (y,x)에 대해서 탐색을 할 필요 없이 바로 값만 계산해서 보내줌
    return dp[y][x]


# 최장거리를 판단해야함
# bfs는 적절하지 않음
def bfs(q, board, visited):
    global MAX_DAY

    while len(q) != 0:
        y, x, bamboo, day = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if 0 <= ny < N and 0 <= nx < N:

                if board[ny][nx] > bamboo and not visited[ny][nx]:
                    q.append((ny, nx, board[ny][nx], day + 1))
                    visited[ny][nx] = True
                    MAX_DAY = max(day + 1, MAX_DAY)


def sol():
    global MAX_DAY

    # for i in range(N):
    #     for j in range(N):
    #         q = deque()
    #         q.append((i, j, board[i][j], 1))

    #         visited = [[False for _ in range(N)] for _ in range(N)]
    #         visited[i][j] = True
    #         bfs(q, board, visited)

    for i in range(N):
        for j in range(N):
            dfs(i,j)

    # map(func,iter)이 iter에 대해서 func 적용한 결과물들이니까
    # max(dp)=>[max(dp[0]),max(dp[1]),max(dp[2])...]
    # 여기에 대해서 다시 max를 하면 2차원 dp에서 최댓값
    return max(map(max,dp))


print(sol())