from sys import stdin
from collections import defaultdict, deque

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, stdin.readline().split())

foods = [[5 for _ in range(N)] for _ in range(N)]

trees = {y: defaultdict(list) for y in range(N)}


added_foods = []

for _ in range(N):
    added_foods.append(list(map(int, stdin.readline().split())))

for _ in range(M):
    y, x, age = map(int, stdin.readline().split())

    trees[y - 1][x - 1].append(age)

for y in range(N):
    for x in range(N):
        trees[y][x].sort()
        trees[y][x] = deque(trees[y][x])

for _ in range(K):
    # 봄
    dead_trees = []

    for y in range(N):
        for x in range(N):
            tree_at_y_x = trees[y][x]

            if not tree_at_y_x:
                continue

            # 소트 아예없이 해보자
            # tree_at_y_x.sort()

            idx = 0
            while idx < len(tree_at_y_x) and foods[y][x] >= tree_at_y_x[idx]:
                foods[y][x] -= tree_at_y_x[idx]
                tree_at_y_x[idx] += 1
                # temp_tree.append(tree_at_y_x[idx]+1)
                idx += 1

            # print(tree_at_y_x)
            n = len(tree_at_y_x)

            for _ in range(n - idx):
                last_tree = tree_at_y_x.pop()
                foods[y][x] += last_tree // 2

    # 여름
    # for y,x,age in dead_trees:
    #     foods[y][x]+=age//2
    # 가을
    new_tree = []
    for y in range(N):
        for x in range(N):
            tree_at_y_x = trees[y][x]

            for age in tree_at_y_x:
                if age % 5 != 0:
                    continue

                for k in range(8):
                    ny, nx = y + dy[k], x + dx[k]

                    if not (0 <= ny < N and 0 <= nx < N):
                        continue

                    trees[ny][nx].appendleft(1)

    # for y in range(N):
    #     for x in range(N):
    #         trees[y][x].sort()

    # 겨울
    for i in range(N):
        for j in range(N):
            foods[i][j] += added_foods[i][j]

tree_count = 0

for i in range(N):
    for j in range(N):
        if trees[i][j]:
            tree_count += len(trees[i][j])


print(tree_count)
