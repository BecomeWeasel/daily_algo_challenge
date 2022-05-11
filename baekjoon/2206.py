from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, stdin.readline().split())

check = [[[False] * (M + 1) for _ in range(N + 1)] for _ in range(2)]
grid = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    s = stdin.readline().rstrip("\n")
    for j in range(M):
        grid[i][j + 1] = int(s[j])


def ans():
    return bfs()


def bfs():
    q = deque()
    # y , x , time , break
    q.append((1, 1, 0, 0))
    check[0][1][1] = True

    while q:
        y, x, time, wall_break = q.popleft()
        if y == N and x == M:
            return time + 1

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if nx > M or ny > N or ny < 1 or nx < 1:
                continue

            if grid[ny][nx] == 1 and wall_break < 1 and not check[1][ny][nx]:
                q.append((ny, nx, time + 1, 1))
                check[1][ny][nx] = True

            if grid[ny][nx] == 0:
                if wall_break == 1 and not check[1][ny][nx]:
                    q.append((ny, nx, time + 1, wall_break))
                    check[1][ny][nx] = True
                elif wall_break != 1 and not check[0][ny][nx]:
                    q.append((ny, nx, time + 1, wall_break))
                    check[0][ny][nx] = True

    return -1


print(ans())
