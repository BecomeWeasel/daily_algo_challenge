from collections import deque
import sys


def ans():
    result = bfs()
    return result


def bfs():
    q = deque()
    visited[1][0] = True
    q.append((0, 1, 1))

    while q:
        line, pos, time = q.popleft()

        # if pos>=N:
        #   return 1

        for nx, new_line in (pos + 1, line), (pos - 1, line), (pos + K, not line):
            # 지금 pos에서 점프를 뛰어서 N칸을 넘어서 아예 벗어나버리거나(클리어)
            # 다음 칸이 N인데 그 칸으로 갈 수 있다면(그 다음번에 클리어)
            if pos + K > N or (nx >= N and board[nx][new_line] == 1):
                return 1
            if nx > time and not visited[nx][new_line] and board[nx][new_line] == 1:
                q.append((new_line, nx, time + 1))
                visited[nx][new_line] = True

        # if not visited[pos+1][line] and  board[pos+1][line]==1:
        #   q.append((line,pos+1,time+1))
        #   visited[pos+1][line]=True

        # if not visited[pos-1][line] and pos-1>=1 and board[pos-1][line]==1 and pos-1>=time:
        #   q.append((line,pos-1,time+1))
        #   visited[pos-1][line]=True

    return 0


N, K = map(int, sys.stdin.readline().split())

visited = [[False] * 2 for _ in range(200001)]
board = [[0] * (2) for _ in range(200001)]

s = sys.stdin.readline()
for i in range(1, N + 1):
    board[i][0] = int(s[i - 1])
s = sys.stdin.readline()
for i in range(1, N + 1):
    board[i][1] = int(s[i - 1])

print(ans())
