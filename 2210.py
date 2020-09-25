from sys import stdin

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count = 0


def ans():
  global count, accum_check

  for i in range(5):
    for j in range(5):
      dfs(i, j, grid[i][j])

  return count


def dfs(y, x, accum_str):
  global grid, check, count, accum_check


  # 이렇게 처리하면 이미 완성한적 있는 6자리 숫자일때
  # return 하지 않고 dfs 탐색을 계속해서 재귀가 끝나질 않음
  # if len(accum_str) == 6 and not accum_str in check:
  #   count += 1
  #   check.add(accum_str)
  #   return

  if len(accum_str) == 6 :
    if not accum_str in check:
      count += 1
      check.add(accum_str)
    return

  for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]

    if ny >= 5 or nx >= 5 or ny < 0 or nx < 0:
      continue

    dfs(ny, nx, accum_str + grid[ny][nx])


grid = [[0] * 5 for _ in range(5)]

for i in range(5):
  grid[i] = list(map(str, stdin.readline().split()))
check = set()
# accum_check = set()

print(ans())
# for item in check:
  # print(item)
