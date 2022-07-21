from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def is_oob(y, x):
    if not (0 <= y < N and 0 <= x < M):
        return True
    return False


def sol():
    board = []
    for _ in range(N):
        board.append(stdin.readline())

    first_y, first_x = -1, -1
    second_y, second_x = -1, -1

    for i in range(N):
        for j in range(M):
            if board[i][j] == "S":
                init_y, init_x = i, j
            elif board[i][j] == "C":
                if first_y != -1:
                    second_y, second_x = i, j
                else:
                    first_y, first_x = i, j
    q = deque()

    q.append((init_y, init_x, -1, 0, 0))
    # q.append((init_y, init_x,-1,0,0,[(init_y, init_x)]))
    # visit=set()
    visit = [[[[False for _ in range(4)] for _ in range(5)] for _ in range(M)] for _ in range(N)]
    visit[init_y][init_x][4][0] = True

    while q:
        y, x, prev_dir, delivery_bit, count = q.popleft()
        # y,x,prev_dir,delivery_bit,count,trace=q.popleft()

        # print(y,x,prev_dir,delivery_bit,count,trace)

        if delivery_bit == 3:
            return count

        for k in range(4):
            if k == prev_dir:
                continue
            ny, nx = y + dy[k], x + dx[k]
            if is_oob(ny, nx):
                continue
            if board[ny][nx] == "#":
                continue

            if visit[ny][nx][k][delivery_bit]:
                continue

            if board[ny][nx] == "C" and first_y == ny and first_x == nx:
                # visit[ny][nx][k][prev_dir][delivery_bit|(1<<0)]=count+1
                visit[ny][nx][k][delivery_bit | (1 << 0)] = True
                q.append((ny, nx, k, delivery_bit | (1 << 0), count + 1))
                # q.append((ny,nx,k,delivery_bit|(1 << 0),count+1,trace[:]+[(ny,nx)]))
            if board[ny][nx] == "C" and second_y == ny and second_x == nx:
                # visit[ny][nx][k][prev_dir][delivery_bit|(1<<1)]=count+1
                visit[ny][nx][k][delivery_bit | (1 << 1)] = True
                q.append((ny, nx, k, delivery_bit | (1 << 1), count + 1))
                # q.append((ny,nx,k,delivery_bit| (1 << 1),count+1,trace[:]+[(ny,nx)]))
            else:
                # visit[ny][nx][k][prev_dir][delivery_bit]=count+1
                visit[ny][nx][k][delivery_bit] = True
                q.append((ny, nx, k, delivery_bit, count + 1))
                # q.append((ny,nx,k,delivery_bit,count+1,trace[:]+[(ny,nx)]))

    # return answer if answer!=987654321 else -1
    return -1


print(sol())
