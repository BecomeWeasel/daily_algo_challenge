from sys import stdin

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

A, B = map(int, stdin.readline().split())
N, M = map(int, stdin.readline().split())


def sol():
  NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

  # grid[1][1][0]=(1,1)에 로봇이 있는지 여부
  # grid[1][1][1]=(1,1)의 로봇이 어디를 보고 있는지 방향,로봇이 없다면 -1
  grid = [[[False, -1] for _ in range(A + 1)] for _ in range(B + 1)]

  robot_status = list()
  # 1번로봇 부터 시작하기 위해서
  robot_status.append([-1, -1, -1])

  for _ in range(N):
    x, y, direction = (stdin.readline().split())
    x, y = map(int, [x, y])
    # 로봇들을 맵에 배치시키기
    grid[y][x] = [True, parse_direct_to_num(direction)]
    robot_status.append([y, x, parse_direct_to_num(direction)])

  ops = list()
  for _ in range(M):
    robot_num, op, iteration = stdin.readline().split()
    ops.append([robot_num, op, iteration])
  for op in ops:
    robot_num, op, iteration = int(op[0]), op[1], int(op[2])

    current_y, current_x, current_dir = get_robot_status(
        robot_num, robot_status)

    if op == 'L':
      # 3->2->1->0->3 ...

      # 3은 0으로 1은 2로 0은 3으로 변환 해주는 함수
      dir_comp = get_3_comp(current_dir)
      dir_comp = (dir_comp + iteration) % 4

      current_dir = get_3_comp(dir_comp)

      # current_dir=current_dir-iteration if current_dir>0 else
      set_robot_status([current_y, current_x, current_dir], robot_num,
                       robot_status)
      grid[current_y][current_x][1] = current_dir

    elif op == 'R':
      # 0->1->2->3->0 ...
      current_dir = (current_dir + iteration) % 4
      set_robot_status([current_y, current_x, current_dir], robot_num,
                       robot_status)
      grid[current_y][current_x][1] = current_dir

    elif op == 'F':

      for step in range(1, iteration + 1):

        # 로봇이 바라보고 있는 방향에 따라서 현재위치에서 얼마를 더하고 뺄지 정해짐
        # 예를 들어 북쪽으로 3번 갈때 ny는 current_y+ 3*1
        ny, nx = current_y + dy[current_dir], current_x + dx[current_dir]

        if ny > B or nx > A or ny == 0 or nx == 0:
          print("Robot " + str(robot_num) + " crashes into the wall")
          return

        # 그자리에 로봇이 있다면
        if grid[ny][nx][0]:
          print("Robot " + str(robot_num) + " crashes into robot " +
                get_robot_num_on_pos(ny, nx, robot_status))
          return
        else:
          set_robot_status([ny, nx, current_dir], robot_num, robot_status)

          grid[ny][nx], grid[current_y][current_x] = grid[current_y][
              current_x], grid[ny][nx]
          current_y, current_x, current_dir = get_robot_status(
              robot_num, robot_status)

  print("OK")


def parse_direct_to_num(direction):
  if direction == 'N':
    return 0
  elif direction == 'E':
    return 1
  elif direction == 'S':
    return 2
  elif direction == 'W':
    return 3


def get_robot_status(robot_num, robot_status):
  return robot_status[robot_num][0], robot_status[robot_num][1], robot_status[
      robot_num][2]


def set_robot_status(robot_info, robot_num, robot_status):
  robot_status[robot_num] = robot_info


def get_robot_num_on_pos(y, x, robot_status):
  for num, robot in enumerate(robot_status):
    if robot[0] == y and robot[1] == x:
      return str(num)


def get_3_comp(num):
  return abs(3 - num)


sol()
