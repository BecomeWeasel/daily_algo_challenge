from sys import stdin


def dfs(v, adjacency, build):

    for node in adjacency[v]:
        if build[node] == 0:
            return False
    return True


def sol():
    N, M, K = map(int, stdin.readline().split())

    adjacency = [list() for _ in range(N + 1)]

    for _ in range(M):
        ori, dest = map(int, stdin.readline().split())
        adjacency[dest].append(ori)

    build = [0 for _ in range(N + 1)]

    order = list()
    for _ in range(K):
        command, num = map(int, stdin.readline().split())
        order.append((command, num))

    for command, num in order:
        if command == 1:
            can_build = dfs(num, adjacency, build)
            if can_build:
                build[num] += 1
            else:
                return "Lier!"
        else:
            if not build[num]:
                return "Lier!"
            else:
                build[num] -= 1

    return "King-God-Emperor"


print(sol())
