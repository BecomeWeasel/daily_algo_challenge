from sys import stdin

# 독특하게 상하우좌로 해야됨
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

R, C, M = map(int, stdin.readline().split())

grid = [[0 for _ in range(C + 1)] for _ in range(R + 1)]

shark = {}


def sol():
    global shark
    answer = 0

    for i in range(1, M + 1):
        r, c, speed, direction, size = map(int, stdin.readline().split())
        shark[i] = (r, c, speed, direction - 1, size)
        grid[r][c] = i

    # 매번 서로 겹쳐지는 애 없나 검사하는건 R*C*C번 하면 되는데 , 그 안에 잇는 상어가 최대 M명이니까 터질 수 있음.
    # 그러지말고 상어가 이동할때 그냥 그 자리에 나보다 작은애가 있으면 덮어쓰기, 나보다 큰애가 있으면 (상어의 크기는 같을 수 없음) 그냥 내가 삭제됨
    # 어차피 속도가 빠르던 느리던, 중간에 만나는게 아니라 이동을 마친 후에 검사하면 되니까 ..

    # 단 가정은 처음에는 모든 상어가 독자적인 자리를 가지고 있다고 했을때

    # 상어의 이동은 최대 M*C 번이니까 , R*C*C번 이동한다 . 근데 속도가 최대 1000이니 한칸씩 간다고 하면 R*C*C*1000=100*100*100*1000

    # 그리고 그 열에서 검사해서 가장 가까운애를 잡으니까 이건 R*C번
    # 정리하면 C(R + R*C*1000)=R*C + R*C*C*1000 = O(RC^2*1000)=O(...) 터지겠는데..? 실제로 TLE남

    # 이걸 해결하기 위해서는 이동하는걸 최적화 해야함.
    # 어차피 두번 왕복하면 (가로든 세로든) 처음자리로 돌아오고 심지어 방향마저 같음.
    # 그니까 상하 움직일때는 세로길이-1 두배만큼 mod 하면 되고 좌우는 가로길이-1 두배만큼 mod

    def next_pos(shark_y, shark_x, direction, speed):

        if direction == 0 or direction == 1:
            speed = speed % ((R - 1) * 2)

        else:
            speed = speed % ((C - 1) * 2)

        for step in range(speed):

            if direction == 1:
                next_y = shark_y + dy[direction]

                if next_y > R:
                    direction = 0
                    shark_y = R - 1
                else:
                    shark_y = next_y

            elif direction == 0:
                next_y = shark_y + dy[direction]

                if next_y < 1:
                    direction = 1
                    shark_y = 2
                else:
                    shark_y = next_y

            elif direction == 3:
                next_x = shark_x + dx[direction]

                if next_x < 1:
                    direction = 2
                    shark_x = 2
                else:
                    shark_x = next_x

            elif direction == 2:
                next_x = shark_x + dx[direction]

                if next_x > C:
                    direction = 3
                    shark_x = C - 1
                else:
                    shark_x = next_x
        return shark_y, shark_x, direction

    for x in range(1, C + 1):
        # (1~R,C)에서 가장 처음만나는 상어 잡아먹기
        for y in range(1, R + 1):
            if grid[y][x] > 0:
                answer += shark[grid[y][x]][4]
                del shark[grid[y][x]]
                break

        # 원래 상어판 초기화
        for y in range(1, R + 1):
            for x in range(1, C + 1):
                grid[y][x] = 0

        # 이제 상어들이 움직임.
        for shark_number in range(1, M + 1):
            if shark_number not in shark:
                continue

            shark_y, shark_x, speed, direction, size = shark[shark_number]

            ny, nx, nd = next_pos(shark_y, shark_x, direction, speed)

            if grid[ny][nx] > 0:
                already_shark_number = grid[ny][nx]

                already_shark = shark[already_shark_number]

                if already_shark[4] > size:
                    del shark[shark_number]
                else:
                    shark[shark_number] = (ny, nx, speed, nd, size)
                    grid[ny][nx] = shark_number
                    del shark[already_shark_number]
            else:
                shark[shark_number] = (ny, nx, speed, nd, size)
                grid[ny][nx] = shark_number

    return answer


print(sol())
