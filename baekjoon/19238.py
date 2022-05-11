from sys import stdin
from collections import deque
import heapq

N, M, fuel_remain = map(int, stdin.readline().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans_flag = True


def find_nearest_passenger(taxi_y, taxi_x, pq):
    global grid, fuel_remain
    q = deque()
    q.append((taxi_y, taxi_x, 0))

    check = [[False] * (N + 1) for _ in range(N + 1)]
    check[taxi_y][taxi_x] = True
    while q:
        pos_y, pos_x, dist = q.popleft()

        # 현재 남아있는 연료보다 멀거나 같은 곳은 탐색할 필요가 없음
        # 왜냐면 현재 남아있는 연료랑 같으면
        # 손님의 출발지와 목적지는 무조건 다르니까(1연료 무조건 소모) 움직일수 없음
        if dist > fuel_remain:
            break

        for k in range(4):
            npos_y = pos_y + dy[k]
            npos_x = pos_x + dx[k]

            # 지도 바깥을 벗어났을때
            if npos_y > N or npos_x > N or npos_y < 1 or npos_x < 1:
                continue

            if not check[npos_y][npos_x] and grid[npos_y][npos_x] != 1:
                check[npos_y][npos_x] = True

                # 음수는 승객이 있는 영역
                # 승객을 발견하면
                if grid[npos_y][npos_x] < 0:
                    heapq.heappush(pq, (dist + 1, npos_y, npos_x, grid[npos_y][npos_x] * -1))

                    # 승객이 없는 빈 공간에 도착했을때
                    # 승객을 찾지 못했다면 그방향으로 탐색 지속
                else:
                    q.append((npos_y, npos_x, dist + 1))


def move_to_dest(taxi_y, taxi_x, pass_dest_y, pass_dest_x):
    # 목적지까지 이동
    check = [[False] * (N + 1) for _ in range(N + 1)]
    q = deque()
    q.append((taxi_y, taxi_x, 0))
    check[taxi_y][taxi_x] = True

    while q:
        pos_y, pos_x, dist = q.popleft()

        for k in range(4):
            npos_y = pos_y + dy[k]
            npos_x = pos_x + dx[k]

            # 지도 바깥을 벗어났을때
            if npos_y > N or npos_x > N or npos_y < 1 or npos_x < 1:
                continue

            if not check[npos_y][npos_x] and grid[npos_y][npos_x] != 1:

                # 손님의 목적지에 도착했을때
                if npos_y == pass_dest_y and npos_x == pass_dest_x:
                    return dist + 1
                else:
                    check[npos_y][npos_x] = True
                    q.append((npos_y, npos_x, dist + 1))

    # 승객을 태운 후 길을 찾을 수 없으면
    return -1


grid = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    grid[i] = list(map(int, stdin.readline().split()))
    grid[i].insert(0, 0)

taxi_y, taxi_x = map(int, stdin.readline().split())

passengers = list()
# 0번 승객은 존재하지 않으므로
passengers.insert(0, 0)
# 몇 명의 승객을 태워서 목적지에 내려줬는지 체크
pass_count = 0

for i in range(1, M + 1):
    pass_ori_y, pass_ori_x, pass_dest_y, pass_dest_x = map(int, stdin.readline().split())

    passengers.append((i, pass_ori_y, pass_ori_x, pass_dest_y, pass_dest_x))

    # 음수는 승객이 있는 영역
    grid[pass_ori_y][pass_ori_x] = -i
    # 탑승 완료 후에는 0으로

while pass_count < M:
    pq = []

    # 만약 택시 출발위치에 바로 승객이 있다면
    if grid[taxi_y][taxi_x] < 0:
        heapq.heappush(pq, (0, taxi_y, taxi_x, grid[taxi_y][taxi_x] * -1))

    # 승객들을 찾아봐야 한다면
    else:
        find_nearest_passenger(taxi_y, taxi_x, pq)

    # 태울만한 승객이 아무도 없으면
    if len(pq) == 0:
        ans_flag = False
        break

    dist, nearest_y, nearest_x, passenger_number = heapq.heappop(pq)

    # 승객을 태우러가다가 연료가 다 떨어질것 같다면
    if dist > fuel_remain:
        ans_flag = False
        break
        # 택시가 손님을 태우러 이동
    else:
        taxi_y, taxi_x = nearest_y, nearest_x
        fuel_remain -= dist

    # 택시를 태웠으니 빈공간으로 바꿈
    grid[nearest_y][nearest_x] = 0

    # 탑승한 손님의 목적지 위치를 구해옴
    pass_dest_y, pass_dest_x = passengers[passenger_number][3], passengers[passenger_number][4]

    dist_to_dest = move_to_dest(taxi_y, taxi_x, pass_dest_y, pass_dest_x)

    # 목적지까지 길을 찾을 수 없으면
    if dist_to_dest == -1:
        ans_flag = False
        break

        # 목적지로 가다가 연료가 다 떨어질것 같다면
    if dist_to_dest > fuel_remain:
        ans_flag = False
        break
    else:
        taxi_y, taxi_x = pass_dest_y, pass_dest_x
        fuel_remain -= dist_to_dest
        fuel_remain += dist_to_dest * 2
        pass_count += 1


if ans_flag:
    print(fuel_remain)
else:
    print(-1)
