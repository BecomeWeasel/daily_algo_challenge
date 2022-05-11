from collections import deque


def solution(board):
    n = len(board)
    answer = 1e9
    # 최단거리가 최소값이 아닐 수 있다. 하지만 근접하게 풀어야한다.

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque()

    # visit[y][x]는 (x,y) 방문시 최소 비용
    visit = [[float("inf") for _ in range(n)] for _ in range(n)]

    # 시작시에는 이전방향을 -1을 줌. 공평하게 무조건 코너를 추가하는 방식
    # 대신에 총 합게에서 500을 차감
    q.append((0, 0, 0, -1))

    while q:
        y, x, cost, prev_dir = q.popleft()
        if y == n - 1 and x == n - 1:
            answer = min(answer, cost)
            continue

        for k in range(4):
            # 이전 방향과 달라졌다면 코너 도는 비용
            curve_cost = 0 if prev_dir == k else 500

            new_cost = cost + 100 + curve_cost

            ny, nx = y + dy[k], x + dx[k]

            # 이전에 방문했던것보다 최소 값 혹은 같은 값으로 방문할수 있으면
            # 중복방문 허용
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1 and new_cost <= visit[ny][nx]:
                # 최소비용으로 갱신
                visit[ny][nx] = new_cost
                q.append((ny, nx, new_cost, k))

    return answer - 500
