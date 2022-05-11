from collections import deque
from itertools import combinations
from sys import stdin

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# dy = [0, 0, -1, 1]
# dx = [1, -1, 0, 0]

# visited = [[[[False for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)]

# visited = set()

board = []

answer = 0

# def is_possible(ny, nx, our, enemy):
#     global board
#     if board[ny][nx] == 'S':
#         return True
#     else:
#         if enemy >= 3:
#             return False
#         return True

# def dfs(y, x, our, enemy, trace, ori_y, ori_x):
# global visited, board, answer
#     if our + enemy == 7:
#         trace.sort()
#         print(trace)
#         s = ''
#         for a, b in trace:
#             s += board[a][b]
#         print(s)
#         # answer += 1
#         return

#     for k in range(4):
#         ny, nx = y + dy[k], x + dx[k]

#         if not (0 <= ny < 5 and 0 <= nx < 5): continue

#         # if visited[ori_y][ori_x][ny][nx]: continue
#         if (ori_y, ori_x, ny, nx) in visited: continue


#         if is_possible(ny, nx, our, enemy):
#             visited.add((ori_y, ori_x, ny, nx))
#             if board[ny][nx] == 'S':
#                 dfs(ny, nx, our + 1, enemy, trace[:] + [(ny, nx)], ori_y, ori_x)
#             else:
#                 dfs(ny, nx, our, enemy + 1, trace[:] + [(ny, nx)], ori_y, ori_x)
#             visited.remove((ori_y, ori_x, ny, nx))
def is_possible(selected_s, selected_y):
    visit_count = 1

    # 만약에 연결되어있다면,
    # 아무 한점에서 출발해도 visit_count는 무조건 7

    target = set()

    for s in selected_s:
        target.add(s)
    for y in selected_y:
        target.add(y)

    init_y, init_x = selected_s[0][0], selected_s[0][1]

    q = deque()

    q.append((init_y, init_x))

    visit = set()
    visit.add((init_y, init_x))

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if not (0 <= ny < 5 and 0 <= nx < 5):
                continue

            if (ny, nx) in visit:
                continue

            if (ny, nx) not in target:
                continue

            q.append((ny, nx))
            visit.add((ny, nx))
            visit_count += 1

    if visit_count == 7:
        return True
    return False


def sol():
    global board, visited, answer

    for _ in range(5):
        board.append(list(stdin.readline().rstrip()))

    # for i in range(5):
    #     for j in range(5):
    #         # visited[i][j][i][j] = True
    #         visited.add((i, j, i, j))

    #         if board[i][j] == 'S':
    #             dfs(i, j, 1, 0, [(i, j)], i, j)
    #         else:
    #             dfs(i, j, 0, 1, [(i, j)], i, j)

    # 탐색 먼저하지말고,
    # 그냥 다 뽑은 다음에 이게 연결되어있는지 확인................................

    s_list = []
    y_list = []

    for i in range(5):
        for j in range(5):
            if board[i][j] == "S":
                s_list.append((i, j))
            else:
                y_list.append((i, j))

    s_len = len(s_list)
    y_len = len(y_list)

    candidate = []

    for s_count in range(4, 8):
        y_count = 7 - s_count

        for selected_s in combinations(s_list, s_count):
            for selected_y in combinations(y_list, y_count):
                if is_possible(selected_s, selected_y):
                    answer += 1
    return answer


print(sol())
