from sys import stdin
from collections import deque


def ans():
    if (A + B + C) % 3 != 0:
        return 0
    return bfs()


def bfs():
    q = deque()
    q.append((A, B, C))
    while q:
        a, b, c = q.popleft()

        if a == b and a == c:
            return 1

        # a와 b 고르기
        if a != b:
            if a > b and not visited[a - b][b + b]:
                q.append((a - b, b + b, c))
                visited[a - b][b + b] = True
            elif a < b and not visited[a + a][b - a]:
                q.append((a + a, b - a, c))
                visited[a + a][b - a] = True

        # b와 c 고르기
        if b != c:
            if b > c and not visited[a][b - c]:
                q.append((a, b - c, c + c))
                visited[a][b - c] = True
            elif b < c and not visited[a][b + b]:
                q.append((a, b + b, c - b))
                visited[a][b + b] = True

    return 0


A, B, C = map(int, stdin.readline().split())

# 여러번의 돌 옮기기를 한다고하더라도 돌의 최대개수는 1500개를 넘을수 없음
# 예를 들어 499 500 500일때
# a와 b를 고르면
# 998 1 500이고
# 이때 1000을 넘으려면 998에 돈을 더넣어야함
# 998과 500을 고르면
# 498 1 1000
# 1000을 넘는 경우는 자주 나옴
# 300 500 601일때
# ->600 200 601
# ->1200 200 1

# 방문배열은 2차원으로 하면 되는데
# A+B+C=N이라고 할때 C=N-A-B이므로
# visited[A][B] 만으로 C의 개수를 알 수 있음
visited = [[False] * 1500 for _ in range(1500)]
visited[A][B] = True

print(ans())
