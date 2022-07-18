from sys import stdin
from collections import deque

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]


N = int(stdin.readline())

left, right = 1000000000, -1
target_count = 0

init_y, init_x = -1, -1


def can_deliver_wrapper(differ, board, height_board, heights):
    global init_y, init_x

    def is_OOB(y, x):
        if not (0 <= y < N and 0 <= x < N):
            return True
        return False

    def can_deliver(minH, maxH):
        # print(f"========\n{minH} , {maxH}")
        global init_y, init_x
        nonlocal board, height_board
        visit = [[False for _ in range(N)] for _ in range(N)]

        q = deque()
        if minH <= height_board[init_y][init_x] <= maxH:
            q.append((init_y, init_x))
        visit[init_y][init_x] = True
        count = 0
        flag = False
        while q:
            y, x = q.popleft()

            for k in range(8):
                ny, nx = y + dy[k], x + dx[k]

                if is_OOB(ny, nx) or visit[ny][nx]:
                    continue

                if not (minH <= height_board[ny][nx] <= maxH):
                    continue

                if board[ny][nx] == "K":
                    count += 1

                if count == target_count:
                    flag = True
                    return True
                visit[ny][nx] = True
                q.append((ny, nx))
        return False

    # f=False

    for h in heights:
        ret = can_deliver(h, h + differ)
        if ret:
            # print(f"differ is {differ} SUC")
            return True
    # print(f"differ is {differ} FAIL")
    return False


def sol():
    global left, right, target_count, init_y, init_x

    board = []
    height_board = []

    for _ in range(N):
        r = stdin.readline()
        board.append(r)

    for _ in range(N):
        r = list(map(int, stdin.readline().split()))
        height_board.append(r)

    heights = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == "P":
                init_y, init_x = i, j
            elif board[i][j] == "K":
                target_count += 1

            heights.append(height_board[i][j])

            # left,right=min(left,board[i][j]),max(right,board[i][j])

    # 생각해보면, 굳이 어떤지점을 돌아야한다 이런건 없음

    # 또 최단거리라는 말도 없음

    # 단순히 모든지점 돌면서 다시 돌아오는데 , 사실 돌아올필요가 있나...?
    # 생각해보니 마지막 방문지점에서 돌아오는 곳에 미친듯이 높은곳이 잇으면 곤란하네 -> 왓던길 되돌아가기

    # K는 최대 49아닌가.....

    # 그럼방문하는 경우의수 매우매우 많음..
    # 피로도 차이 다 계산하지말고 , 미리 고도 정하고 가는것도 ..

    # 결국 파라메트릭 서치 아닌가

    # 높이 정해놓고, 이 높이로 모든 집 방문할 수 있니? 라고 하면 높이를 더 줄여보고 ................

    # 근데 높이의 최소가 아니라 차의 최소인데 ...? ㅅㅂ좃댓다

    # 피로도 = 고도의 차
    # 3 = 4-1 or 5-2 or 6-3 or 7-4 or ...

    # 고도 최대 100만 =~ 피로도 log2 100-> 20

    # 피로도 k -> a ~ a+k or (a)-1~(a+k)-1

    # 처음 고도 구간이 쫙 주어져있으면

    # 1 2 4 8 11 18 20 24

    # k = 4 -> 1~5 2~6 4~8

    # 최대 차이 1백만이니 이분탐색시 20정도

    # 매 diff(mid)마다 , N^2번 탐색을 수행하는데 탐색은 N^2..
    # O(20*N^4)=1.25억 정도 ..

    heights.sort()

    right = heights[-1] - heights[0]
    left = right

    for i in range(len(heights) - 1):
        left = min(left, heights[i + 1] - heights[i])

    # print(heights)

    # print(left,right)

    answer = 987654321

    while left <= right:
        mid = (left + right) // 2

        if can_deliver_wrapper(mid, board, height_board, heights):
            right = mid - 1
            answer = min(mid, answer)
        else:
            left = mid + 1

    return answer


print(sol())
