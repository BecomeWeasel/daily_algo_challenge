from sys import stdin
from itertools import product

N = int(stdin.readline())

# 최대 5번이니 총 경우의 수는 4^5=2^10=1024 한번의 이동에 최대 20*20 소요되니 1024*400

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():
    max_result = 0

    og_board = []

    for _ in range(N):
        og_board.append(list(map(int, stdin.readline().split())))

    def movement(board, dir_):
        global N

        # up
        if dir_ == 0:
            for x in range(N):
                og_list = []
                for y in range(N):
                    og_list.append(board[y][x])

                tmp = [0 for _ in range(N)]

                idx = 0
                for num in og_list:
                    if num == 0:
                        continue
                    elif tmp[idx] == 0:
                        tmp[idx] = num
                    elif tmp[idx] != num:
                        idx += 1
                        tmp[idx] = num
                    elif tmp[idx] == num:
                        tmp[idx] = 2 * tmp[idx]
                        idx += 1
                for y in range(N):
                    board[y][x] = tmp[y]

        # down
        elif dir_ == 1:
            for x in range(N):
                og_list = []

                for y in range(N - 1, -1, -1):
                    og_list.append(board[y][x])
                tmp = [0 for _ in range(N)]

                idx = N - 1
                for num in og_list:
                    if num == 0:
                        continue
                    elif tmp[idx] == 0:
                        tmp[idx] = num
                    elif tmp[idx] != num:
                        idx -= 1
                        tmp[idx] = num
                    elif tmp[idx] == num:
                        tmp[idx] = 2 * tmp[idx]
                        idx -= 1
                for y in range(N - 1, -1, -1):
                    board[y][x] = tmp[y]

        # left
        elif dir_ == 2:
            for y in range(N):
                og_list = board[y][:]
                tmp = [0 for _ in range(N)]
                '''
                [0,0,2,0,0,2,0,4]
                를 대상으로 같은 크기만큼의 tmp 배열만듬
                원래 리스트를 왼쪽으로 loop 돌면서

                0이 아닌 숫자를 만나면 tmp에 집어넣고 idx 조정
                현재 들어갈 자리에 같은 숫자만나면 합치고 idx 조정
                현재 들어갈 자리에 다른 숫자만나면 다음 칸에 집어 넣음
                
        
                '''
                idx = 0
                for num in og_list:
                    if num == 0:
                        continue
                    # 그냥 빈공간이면 집어넣고
                    # 다음이 중복될수 있으니 idx 그대로
                    elif tmp[idx] == 0:
                        tmp[idx] = num
                    # 들어갈곳에 0이 아니고 나랑 다른 숫자면 다음 칸에 쓰기
                    elif tmp[idx] != num:
                        idx += 1
                        tmp[idx] = num
                    elif tmp[idx] == num:
                        tmp[idx] = 2 * tmp[idx]
                        idx += 1
                board[y] = tmp

        # right
        elif dir_ == 3:
            for y in range(N):
                og_list = board[y][:]
                og_list.reverse()

                tmp = [0 for _ in range(N)]

                idx = 0
                for num in og_list:
                    if num == 0:
                        continue
                    elif tmp[idx] == 0:
                        tmp[idx] = num
                    elif tmp[idx] != num:
                        idx += 1
                        tmp[idx] = num
                    elif tmp[idx] == num:
                        tmp[idx] = 2 * tmp[idx]
                        idx += 1

                tmp.reverse()
                board[y] = tmp

    case_list = [[x for x in range(4)] for _ in range(5)]

    copy_board = []
    for row in og_board:
        copy_board.append(row[:])

    def print_board(board):
        print("=======")
        for row in board:
            print(row)
        print("=======")

    # 매 수행마다 상 하 좌 우 수행 경우의 수
    for combi in product(*case_list):
        copy_board = []
        for row in og_board:
            copy_board.append(row[:])
        for dir_ in combi:
            movement(copy_board, dir_)

        max_result = max(max_result, max(map(max, copy_board)))

    return max_result


print(sol())
