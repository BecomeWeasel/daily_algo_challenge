from sys import stdin


def sol():

    H, W = map(int, stdin.readline().split())
    input_grid = []
    for _ in range(H):
        input_grid.append(stdin.readline().rstrip())
    grid_dp = [[-1 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W - 1, -1, -1):
            if input_grid[i][j] == "c":
                for k in range(j, W, 1):
                    if grid_dp[i][k] != -1 and grid_dp[i][k] <= 0 + k - j:
                        break
                    grid_dp[i][k] = 0 + k - j

    for i in range(H):
        print(" ".join(map(str, grid_dp[i])))


sol()
