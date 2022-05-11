from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(board, r, c):
    def isEnd(s) -> bool:
        for c in s:
            if c != "0":
                return False
        return True

    def OOB(y, x) -> bool:
        if (not 0 <= y < 4) or (not 0 <= x < 4):
            return True
        return False

    def isOnEdgeByDirection(y, x, d) -> bool:

        if d == 0:
            if y == 0:
                return True
        elif d == 1:
            if y == 3:
                return True
        elif d == 2:
            if x == 0:
                return True
        elif d == 3:
            if x == 3:
                return True
        return False

    # 바뀌는 상황 :
    # 카드판의 상황,현재 커서의 위치 , 현재 뒤집었는지? 아니면 안뒤집엇는지 ( 2장째 기다리는중인지 뒤집었다면 커서 위치)

    # 구하는 것 : 최소 회수 이동

    def serialize(board) -> str:
        ret = ""
        for r in board:
            for num in r:
                ret += str(num)

        return ret

    def switchTo0(s: str, num: str) -> int:

        return s.replace(num, "0")

    def idxConverter(y, x) -> int:
        return 4 * y + x

    visit = set()

    # 보드의 상태 ,커서의 위치 , 커서가 카드를 뒤집었는지 , 뒤집힌 카드가 있다면 그 위치
    visit.add((serialize(board), (r, c), False, (-1, -1)))
    q = deque()
    q.append((serialize(board), r, c, False, -1, -1, 0))

    while q:
        b, y, x, isFlipped, f_y, f_x, count = q.popleft()

        # 모든 카드를 뒤집었는지
        # 여기서 체크하면 시간 더걸림
        # if isEnd(b):
        #     return count

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if OOB(ny, nx):
                continue

            while b[idxConverter(ny, nx)] == "0" and not isOnEdgeByDirection(ny, nx, k):
                ny, nx = ny + dy[k], nx + dx[k]

            if (b, (ny, nx), isFlipped, (f_y, f_x)) in visit:
                continue

            visit.add((b, (ny, nx), isFlipped, (f_y, f_x)))
            q.append((b, ny, nx, isFlipped, f_y, f_x, count + 1))

        # 상하좌우 네방향 이동

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if OOB(ny, nx):
                continue

            if (b, (ny, nx), isFlipped, (f_y, f_x)) in visit:
                continue

            visit.add((b, (ny, nx), isFlipped, (f_y, f_x)))
            q.append((b, ny, nx, isFlipped, f_y, f_x, count + 1))

        # 현재 한장은 뒤집은 상태에서 다른것 뒤집으려 할때
        if isFlipped:
            # 카드 짝 찾는데 성공하면
            # 0으로 뒤집고
            if b[idxConverter(f_y, f_x)] == b[idxConverter(y, x)] and (f_y, f_x) != (y, x):

                b = switchTo0(b, b[idxConverter(f_y, f_x)])

                # 여기서 끝낼수있음

                if isEnd(b):
                    return count + 1

                # print(b)
                visit.add((b, (y, x), False, (-1, -1)))
                q.append((b, y, x, False, -1, -1, count + 1))

            # 짝은 안맞으면
            else:

                if (b, (y, x), False, (-1, -1)) in visit:
                    continue
                visit.add((b, (y, x), False, (-1, -1)))
                q.append((b, y, x, False, -1, -1, count + 1))
        # 아직 뒤집지 않은 상태
        # 이제 뒤집기
        else:
            if (b, (y, x), True, (y, x)) in visit:
                continue

            visit.add((b, (y, x), True, (y, x)))
            q.append((b, y, x, True, y, x, count + 1))


# print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))

# print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0))
