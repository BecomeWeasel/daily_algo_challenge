from sys import stdin

H, W = map(int, stdin.readline().split())

blocks = list(map(int, stdin.readline().split()))


def sol():

    rain = 0

    # 0번과 W-1번 block위치는 물을 계산 안함
    # 물이 차오를수가 없음

    for i in range(1, W - 1, 1):
        left, right = 0, 0

        for j in range(0, i, 1):
            left = max(left, blocks[j])
        for j in range(i, W, 1):
            right = max(right, blocks[j])

        rain_height = min(left, right)

        rain = rain + max(0, rain_height - blocks[i])

    return rain


print(sol())
