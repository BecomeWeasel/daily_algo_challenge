from sys import stdin

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

N, M, dice_y, dice_x, K = map(int, stdin.readline().split())


def sol():
    global dice_x, dice_y
    dice = [0 for _ in range(6)]

    board = []

    for _ in range(N):
        board.append(list(map(int, stdin.readline().split())))

    # 명령들
    inst = list(map(int, stdin.readline().split()))

    for order, direction in enumerate(inst):
        new_y, new_x = dice_y + dy[direction], dice_x + dx[direction]

        # 지도를 벗어나려하면
        if not 0 <= new_y < N or not 0 <= new_x < M:
            continue

        roll_dice(direction, dice)

        # 이동할 칸에 쓰여있는 수가 0이면
        # 주사위 바닥면의 수가 칸에 복사
        if board[new_y][new_x] == 0:
            board[new_y][new_x] = dice[5]

        # 0이 아니라면
        # 칸에 쓰여져있는 수가 주사위 바닥면으로 복사
        # 칸은 0이 됨
        else:
            dice[5] = board[new_y][new_x]
            board[new_y][new_x] = 0

        dice_y, dice_x = new_y, new_x

        # 그 후 상단의 값을 출력
        print(dice[0])


def roll_dice(direction, dice):

    # 주사위를 동쪽으로 굴리면
    if direction == 1:
        dice[2], dice[5], dice[3], dice[0] = dice[0], dice[2], dice[5], dice[3]
    # 서쪽
    elif direction == 2:
        dice[2], dice[5], dice[3], dice[0] = dice[5], dice[3], dice[0], dice[2]
    # 북쪽
    elif direction == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    # 남쪽
    elif direction == 4:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]


sol()
