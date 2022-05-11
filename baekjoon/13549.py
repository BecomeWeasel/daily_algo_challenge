from sys import stdin
from collections import deque
from queue import PriorityQueue


def ans():
    return bfs(N, K)


def bfs(N, K):
    q = deque()
    q.append((N, 0))
    visited[N] = 0
    r_value = 987654321

    while q:
        pos, cnt = q.popleft()

        if pos == K:
            return cnt
            # r_value = min(r_value, cnt)
            # continue

        if pos * 2 <= 100000 and visited[pos * 2] == -1 or visited[pos * 2] >= cnt:
            # q.append((pos * 2, cnt))
            # 가중치가 모두 동일하지 않을때
            # 0-1 BFS라고 하는데 이때는
            # 가중치가 0인 간선을 맨 앞에 넣어야함.
            # 이럴때 naive한 구현의 반레는
            # 4 6
            q.appendleft((pos * 2, cnt))
            visited[pos * 2] = cnt

        if pos + 1 <= 100000 and visited[pos + 1] == -1:
            q.append((pos + 1, cnt + 1))
            visited[pos + 1] = cnt + 1

        if pos - 1 >= 0 and visited[pos - 1] == -1:
            q.append((pos - 1, cnt + 1))
            visited[pos - 1] = cnt + 1

    # return r_value


N, K = map(int, stdin.readline().split())

# visited[i] : i번째에 방문한 시간
# -1이라면 방문하지 않았음
visited = [-1 for _ in range(100001)]

result_list = []
print(ans())
