from sys import stdin
from queue import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

R, C, N = map(int, stdin.readline().split())


def sol():
    grid = [["*", False, -1] * C for _ in range(R)]

    # 초기 격자판 상태 입력받기
    for i in range(R):
        string = stdin.readline().rstrip("\n")
        for j in range(C):
            grid[i][j] = string[j]

    # 폭탄의 위치와 시간 기록
    boom_queue = deque()

    for i in range(R):
        for j in range(C):
            if grid[i][j] == "O":
                # 초기 폭탄이 설치된 위치에 시간을 0으로 기록
                grid[i][j] = ["O", True, 0]

    # 1초뒤에 아무일도 일어나지 않으니
    elapsed_time = 1

    while elapsed_time < N:

        elapsed_time += 1
        for i in range(R):
            for j in range(C):
                # 비어있는 칸에 폭탄설치하기
                if grid[i][j][0] == ".":
                    # 폭탄설치 시간 기록하기
                    # True는 폭탄 설치 유무
                    grid[i][j] = ["O", True, elapsed_time]

        if elapsed_time == N:
            break

        for i in range(R):
            for j in range(C):
                # 폭탄을 설치한지 3초가 지났다면
                if grid[i][j][1] == True and grid[i][j][2] == elapsed_time - 2:
                    booom(i, j, grid)

        elapsed_time += 1

    for i in range(R):
        result = ""
        for j in range(C):
            result += grid[i][j][0]
        print(result)


def booom(y, x, grid):

    # 현재 폭탄이 설치된 시간
    current_time = grid[y][x][2]
    # 현재 폭탄설치된 곳을 미리 터트리고 시작
    grid[y][x] = [".", False, -1]

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]

        if ny < 0 or nx < 0 or ny >= R or nx >= C:
            continue

        # 터질곳에 폭탄이 있지만 그 폭탄도 곧 터져야할 폭탄일경우
        if grid[ny][nx][1] == True and grid[ny][nx][2] == current_time:
            continue
        else:
            grid[ny][nx] = [".", False, -1]


sol()
