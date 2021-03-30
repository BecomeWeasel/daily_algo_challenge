from sys import stdin


def ans():
  grid = [[0 for _ in range(101)] for _ in range(101)]

  paper_set = list()
  for _ in range(N):
    x, y = map(int, stdin.readline().split())
    paper_set.append([x, y])

  for square in paper_set:
    for i in range(10):
      for j in range(10):
        grid[square[1] + i][square[0]+j] = 1

  grid_count=0
  for i in range(101):
    for j in range(101):
      if grid[i][j]==1:
        grid_count+=1
  print(grid_count)


N = int(stdin.readline())
ans()
