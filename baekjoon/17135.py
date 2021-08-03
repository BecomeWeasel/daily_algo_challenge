from sys import stdin
from collections import deque
from itertools import combinations

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():
    N, M, D = map(int, stdin.readline().split())
    max_kill = -1
    board = []

    def OOB(y, x):
        nonlocal N, M, D
        # 맵 밖으로 벗어날때
        if not (0 <= y < N) or not (0 <= x < M):
            return True
        # 궁수라인이면
        if y == N:
            return True
        return False

    for _ in range(N):
        board.append(list(map(int, stdin.readline().split())))

    def combi_kill(combi):
        nonlocal board, N, M, D
        kill = 0
        cp_board = []
        for r in board:
            cp_board.append(r[:])
        archer_line = [0 for _ in range(M)]

        for a in combi:
            archer_line[a] = 9
        cp_board.append(archer_line)
        '''
        print()
        print()
        for r in cp_board:
            print(r)
        '''
        def bfs(q: deque, visit: set):
            nonlocal cp_board, N, M, D
            target = []
            while q:
                y, x, dist = q.popleft()

                if dist == D:
                    continue

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]

                    if OOB(ny, nx):
                        continue

                    if (ny, nx) not in visit:
                        if cp_board[ny][nx] == 1:
                            target.append((dist, ny, nx))
                        visit.add((ny, nx))
                        q.append((ny, nx, dist + 1))
            return sorted(target, key=lambda x: (x[0], x[2]))

        while True:

            if sum(sum(cp_board[:N], [])) == 0:
                return kill

            enemy_list = []

            q = deque()
            # 첫번째 궁수
            q.append((N, combi[0], 0))
            target = []
            visit = set()
            visit.add((N, combi[0]))

            t = bfs(q, visit)
            if len(t) != 0:
                enemy_list.append(t[0])

            q = deque()
            # 두번째 궁수
            q.append((N, combi[1], 0))
            target = []
            visit = set()
            visit.add((N, combi[1]))

            t = bfs(q, visit)
            if len(t) != 0:
                enemy_list.append(t[0])

            q = deque()
            # 세번째 궁수
            q.append((N, combi[2], 0))
            target = []
            visit = set()
            visit.add((N, combi[2]))

            t = bfs(q, visit)
            if len(t) != 0:
                enemy_list.append(t[0])

            for enemy in enemy_list:
                dist, y, x = enemy
                if cp_board[y][x] == 1:
                    cp_board[y][x] = 0
                    kill += 1

            # 성 벽에 닿을 애들은 제외시키기
            for x in range(M):
                if cp_board[N][x] == 1:
                    cp_board[N][x] = 0
            for x in range(M):
                for y in range(N - 2, -1, -1):
                    cp_board[y + 1][x] = cp_board[y][x]
                cp_board[0][x] = 0

    for combi in combinations([i for i in range(M)], 3):
        max_kill = max(combi_kill(combi), max_kill)

    return max_kill


print(sol())
