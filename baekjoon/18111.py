from sys import stdin

N, M, B = map(int, stdin.readline().split())


def ans():

  grid=[list(map(int,stdin.readline().split())) for _ in range(N)]

  
  min_time = 9876543219876543219876
  max_height = -1

  for h in range(257):
    stack_up = 0
    stack_down = 0
    for i in range(N):
      for j in range(M):

        if grid[i][j]>h:
          stack_down+=grid[i][j]-h
        else:
          stack_up+=h-grid[i][j]


    if stack_down + B < stack_up:
      continue
    # 깎은 후 인벤토리에 넣은것과 이미 인벤토리에 넣은것으로
    # 쌓아올려서 높이를 맞출수 있으면
    # 깎는데는 2초, 쌓는데는 1초
    time = 2 * stack_down + stack_up

    # 시간을 경신했다면
    if min_time >= time:
      # 높이도 경신해줌, 단 시간이 같을때는 높이가 우선
      max_height = h
      min_time = time

  print(' '.join(list(map(str, [min_time, max_height]))))


ans()
