from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


class node:
    def __init__(self, pos_x, pos_y, r):
        self.posx = pos_x
        self.posy = pos_y
        self.r = r


def bfs(i):
    q = deque()
    q.append((i))

    while q:
        src = q.popleft()

        for dest in range(N):
            if not visited[dest] and connection[src][dest]:
                q.append((dest))
                visited[dest] = True


T = int(stdin.readline())
visited = [[]]

while T:
    N = int(stdin.readline())
    visited = [False for _ in range(N + 1)]
    connection = [[False] * N for _ in range(N)]
    nodes = []
    for _ in range(N):
        pos_x, pos_y, r_value = map(int, stdin.readline().split())

        nodes.append(node(pos_x, pos_y, r_value))

        # start_x = 0
        # start_y = 0

        # end_x = 0
        # end_y = 0

        # if pos_x - r_value < 0:
        #   start_x = 0
        # else:
        #   start_x = pos_x - r_value

        # if pos_x + r_value > 4999:
        #   end_x = 4999
        # else:
        #   end_x = pos_x + r_value

        # if pos_y - r_value < 0:
        #   start_y = 0
        # else:
        #   start_y = pos_y - r_value

        # if pos_y + r_value > 4999:
        #   end_y = 4999
        # else:
        #   end_y = pos_y + r_value

        # start_x = (pos_x - r_value < 0 and 0 or pos_x-r_value)
        # end_x = (pos_x + r_value - 1 > 4999 and 4999 or pos_x + r_value - 1)

        # start_y = pos_y - r_value < 0 and 0 or pos_y - r_value
        # end_y = pos_y + r_value - 1 > 4999 and 4999 or pos_y + r_value - 1

        # for i in range(start_y, end_y + 1):
        # for j in range(start_x, end_x + 1):
        # grid[i][j] = True
    for i in range(N):
        for j in range(i + 1, N):
            diff_x = nodes[i].posx - nodes[j].posx
            diff_y = nodes[i].posy - nodes[j].posy
            sum_r = nodes[i].r + nodes[j].r

            if (diff_x * diff_x + diff_y * diff_y) <= (sum_r * sum_r):
                connection[i][j] = connection[j][i] = True

    cnt = 0

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            bfs(i)
            cnt += 1

    print(cnt)

    T -= 1
