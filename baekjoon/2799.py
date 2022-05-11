from sys import stdin

M, N = map(int, stdin.readline().split())


def ans():
    windows_type = [0] * 5

    grid = [["#"] * (5 * N + 1) for _ in range(5 * M + 1)]

    for i in range(5 * M + 1):
        grid[i] = list(map(str, stdin.readline()))

    for i in range(1, 5 * M + 1, 5):
        for j in range(1, 5 * N + 1, 5):
            blind_type = sum(1 for x in range(4) if grid[i + x][j] == "*")
            windows_type[blind_type] += 1

    print(" ".join(map(str, windows_type)))


ans()
