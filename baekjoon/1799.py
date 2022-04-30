from sys import stdin

N = int(stdin.readline())

board = []
answer = -1

left_top = [False for _ in range(100)]
right_top = [False for _ in range(100)]


def is_possible(y, x):
    if left_top[y + x] or right_top[x - y + N - 1]:
        return False

    return True


def dfs(y, x, count):
    global answer, left_top, right_top

    answer = max(answer, count)

    if not (0 <= y < N and 0 <= x < N):
        return

    # if board[y][x] == 1:
    #     temp = count + 1
    # else:
    #     temp = count

    # answer = max(answer, temp)

    # 다음 칸 계산하기

    if N % 2 == 0:
        if x == N - 1:
            next_y = y + 1
            next_x = 0
        elif x == N - 2:
            next_y = y + 1
            next_x = 1
        else:
            next_y = y
            next_x = x + 2
    else:
        if x == N - 1:
            next_y = y + 1
            next_x = 1
        elif x == N - 2:
            next_y = y + 1
            next_x = 0
        else:
            next_y = y
            next_x = x + 2

    if not (0 <= next_y < N and 0 <= next_x < N):
        return

    if board[next_y][next_x] != 1:
        dfs(next_y, next_x, count)
        return

    # 요기가 문제
    # 만약 dfs 함수 초입에
    # count 체크하면 , 두번오름
    # 만약 dfs 인자로 넘겨주면
    # 초반처리가 안됨.
    if not is_possible(next_y, next_x):
        dfs(next_y, next_x, count)
        return

    left_top[next_y + next_x] = True
    target = next_x - next_y + N - 1
    # 최소는 0,N-1 일때니까 , 여기에 N-1만큼 더해서 0보다 크거나 같게만들기
    # 반대로 최대는 N-1,0 인데 이때 N-1 더하면 2N-2
    right_top[target] = True

    # answer = max(answer, temp + 1)

    # ny nx에 비숍 놓겟다는 의미
    dfs(next_y, next_x, count + 1)

    left_top[next_y + next_x] = False
    right_top[target] = False

    # 이번엔 이칸에 안놓기
    dfs(next_y, next_x, count)


def sol():
    global board, answer

    for _ in range(N):
        board.append(list(map(int, stdin.readline().split())))

    if N == 1:
        if board[0][0] == 1:
            return 1
        else:
            return 0
    else:
        if board[0][0] == 1:
            left_top[0] = True
            right_top[N - 1] = True
            dfs(0, 0, 1)
            left_top[0] = False
            right_top[N - 1] = False
            # 이부분 빼먹으면, (0,0)칸에는 무조건 놓는다는건데, 그건 말이 안됨
            dfs(0, 0, 0)
        else:
            dfs(0, 0, 0)
        ret = answer

        answer = 0

        if board[0][1] == 1:
            left_top[1] = True
            right_top[1 - 0 + N - 1] = True
            dfs(0, 1, 1)
            left_top[1] = False
            right_top[1 - 0 + N - 1] = False
            # 이부분 빼먹으면, (0,1)칸에는 무조건 놓는다는건데, 그건 말이 안됨
            dfs(0, 1, 0)
        else:
            dfs(0, 1, 0)
        ret += answer

        return ret


print(sol())
