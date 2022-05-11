from sys import stdin

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(stdin.readline())


def ans():
    grid = [[0 for _ in range(C)] for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]

    binary_string = list()

    # 문자를 5자리 이진수로 변환 (공백은 00000으로)
    for char in message:
        if char == " ":
            binary_string.append(bin(0)[2:].zfill(5))
        else:
            binary_string.append(bin(ord(char) - 65 + 1)[2:].zfill(5))

    pos_x, pos_y, direct = 0, 0, 0

    for i, binary in enumerate(binary_string):
        for j, single in enumerate(binary):
            grid[pos_y][pos_x] = int(single)
            visited[pos_y][pos_x] = True

            npos_x, npos_y = pos_x + dx[direct], pos_y + dy[direct]

            # 이미 가봤던곳을 가거나 맵을 벗어나면
            if npos_x >= C or npos_y >= R or npos_x < 0 or npos_y < 0 or visited[npos_y][npos_x]:
                direct = (direct + 1) % 4
                npos_x, npos_y = pos_x + dx[direct], pos_y + dy[direct]

            pos_x, pos_y = npos_x, npos_y

    result = ""
    for row in grid:
        result += "".join(map(str, row))

    print(result)


for _ in range(T):
    inputs = stdin.readline().rstrip("\n")
    R, C = map(int, inputs.split()[:2])

    # 문자가 시작되는 지점을 찾기
    c_space = 0
    end = 0
    for i, char in enumerate(inputs):
        if char == " ":
            c_space += 1
            if c_space == 2:
                end = i
                break

    message = "".join(inputs[end:]).lstrip()
    ans()
