from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(board):
    N = len(board)

    answer = float('inf')

    q = deque()

    # y1,x1,y2,x2,count
    q.append((((0, 0), (0, 1)), 0))

    visit = set()

    # out of bound 이거나 갈 수 없는 곳이라면
    def OOB(p1, p2):
        nonlocal board

        for p in [p1, p2]:
            if not (0 <= p[0] < N) or not (0 <= p[1] < N):
                return False
            if board[p[0]][p[1]] == 1:
                return False
        return True

    visit.add(((0, 0), (0, 1)))

    while q:
        pos, count = q.popleft()

        y1, x1 = pos[0][0], pos[0][1]
        y2, x2 = pos[1][0], pos[1][1]

        if (y1, x1) == (N - 1, N - 1) or (y2, x2) == (N - 1, N - 1):
            return count

        for k in range(4):
            if not OOB([y1 + dy[k], x1 + dx[k]], [y2 + dy[k], x2 + dx[k]]):
                continue

            if ((y1 + dy[k], x1 + dx[k]), (y2 + dy[k], x2 + dx[k])) in visit:
                continue

            visit.add(tuple(sorted(((y1 + dy[k], x1 + dx[k]), (y2 + dy[k], x2 + dx[k])), key=lambda x: (x[0], x[1]))))
            q.append((((y1 + dy[k], x1 + dx[k]), (y2 + dy[k], x2 + dx[k])), count + 1))

        # 가로일때 회전
        if y1 == y2:
            # y2 축으로 y1이 왼쪽에서 위쪽 회전시 가능 한지 체크
            if OOB((y1 - 1, x1), (y1 - 1, x1 + 1)) and ((y1 - 1, x1 + 1), (y2, x2)) not in visit:
                visit.add(((y1 - 1, x1 + 1), (y2, x2)))
                q.append((((y1 - 1, x1 + 1), (y2, x2)), count + 1))
            # y2 축으로 y1이 왼쪽에서 아래쪽으로 회전
            if OOB((y1 + 1, x1), (y1 + 1, x1 + 1)) and ((y2, x2), (y1 + 1, x1 + 1)) not in visit:
                visit.add(((y2, x2), (y1 + 1, x1 + 1)))
                q.append((((y2, x2), (y1 + 1, x1 + 1)), count + 1))

            # y1 축으로 y2가 오른쪽에서 위쪽으로 회전
            if OOB((y2 - 1, x2), (y2 - 1, x2 - 1)) and ((y2 - 1, x2 - 1), (y1, x1)) not in visit:
                visit.add(((y2 - 1, x2 - 1), (y1, x1)))
                q.append((((y2 - 1, x2 - 1), (y1, x1)), count + 1))

            # y1 축으로 y2가 오른쪽에서 아래로 회전
            if OOB((y2 + 1, x2), (y2 + 1, x2 - 1)) and ((y1, x1), (y2 + 1, x2 - 1)) not in visit:
                visit.add(((y1, x1), (y2 + 1, x2 - 1)))
                q.append((((y1, x1), (y2 + 1, x2 - 1)), count + 1))

        else:
            # y1 축으로 y2가 반시계
            if OOB((y2, x2 - 1), (y2 - 1, x2 - 1)) and ((y2 - 1, x2 - 1), (y1, x1)) not in visit:
                visit.add(((y2 - 1, x2 - 1), (y1, x1)))
                q.append((((y2 - 1, x2 - 1), (y1, x1)), count + 1))

            # y1 축으로 y2가 시계
            if OOB((y2, x2 + 1), (y2 - 1, x2 + 1)) and ((y1, x1), (y2 - 1, x2 + 1)) not in visit:
                visit.add(((y1, x1), (y2 - 1, x2 + 1)))
                q.append((((y1, x1), (y2 - 1, x2 + 1)), count + 1))

            # y2 축으로 y1이 시계
            if OOB((y1, x1 + 1), (y1 + 1, x1 + 1)) and ((y2, x2), (y1 + 1, x1 + 1)) not in visit:
                visit.add(((y2, x2), (y1 + 1, x1 + 1)))
                q.append((((y2, x2), (y1 + 1, x1 + 1)), count + 1))

            # y2 축으로 y1이 반시계
            if OOB((y1, x1 - 1), (y1 + 1, x1 - 1)) and ((y1 + 1, x1 - 1), (y2, x2)) not in visit:
                visit.add((((y1 + 1, x1 - 1), (y2, x2))))
                q.append((((y1 + 1, x1 - 1), (y2, x2)), count + 1))


print(
    solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
