from collections import deque


def solution(places):
    answer = []

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for place in places:

        people = []

        board = []

        for row in place:
            board.append(row)

        for i in range(5):
            for j in range(5):
                if board[i][j] == "P":
                    people.append((i, j))

        safe_flag = True

        for p in people:
            q = deque()
            q.append((p[0], p[1], 0))
            visit = set()
            visit.add((p[0], p[1]))
            while q:
                y, x, dist = q.popleft()

                if dist == 2:
                    continue

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]

                    if not (0 <= ny < 5) or not (0 <= nx < 5):
                        continue

                    if (ny, nx) not in visit and board[ny][nx] != "X":
                        if board[ny][nx] == "P":
                            safe_flag = False
                        q.append((ny, nx, dist + 1))
                        visit.add((ny, nx))

        if safe_flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer
