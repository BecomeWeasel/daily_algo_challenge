from sys import stdin
from queue import deque

N, K = map(int, stdin.readline().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():
    grid = [[0] * N for _ in range(N)]

    for i in range(N):
        grid[i] = list(map(int, stdin.readline().split()))

    # S 초뒤 grid[Y-1][X-1]
    S, X, Y = map(int, stdin.readline().split())

    # virus_queue=PriorityQueue()
    virus_queue = deque()

    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                # 낮은 순서대로 퍼지니까 바이러스의 번호순대로 집어넣어야함.
                virus_queue.append([grid[i][j], i, j])

                # 바이러스 큐를 PQ로 선언하면 낮은 순의 바이러스를 바로 앞에서 가져오면되지만
                # put 할때마다 정렬이 일어나므로 매우 비효율적 -> TLE
                # virus_queue.put((grid[i][j],i,j))
    virus_queue = deque(sorted(virus_queue, key=lambda x: (x[0])))

    for current_time in range(S):

        # 더 이상 퍼질곳이 없다면 종료
        if len(virus_queue) == 0:
            break

        # 다음 시간에 퍼질 바이러스들의 모임
        next_virus_queue = deque()
        # PQ가 empty 될때까지 확산
        while len(virus_queue) != 0:
            virus_num, y, x = virus_queue.popleft()

            spread_virus(virus_num, y, x, next_virus_queue, grid)

        # PrioirityQueue처럼 삽입마다 정렬할 필요 없이 한번 바이러스 퍼트리는 사이클이 지난 다음에
        # 정렬해도 됨.
        virus_queue = deque(sorted(next_virus_queue, key=lambda x: x[0]))

    return grid[X - 1][Y - 1]


def spread_virus(virus_num, y, x, pq, grid):

    for k in range(4):

        ny, nx = y + dy[k], x + dx[k]

        # 시험관 크기를 벗어나는 경우
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue

        if grid[ny][nx] == 0:
            grid[ny][nx] = virus_num
            pq.append([virus_num, ny, nx])


print(sol())
