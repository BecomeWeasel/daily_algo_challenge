from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())


def sol():
    board = [list(map(int, stdin.readline().split())) for _ in range(N)]

    stores = list()
    houses = list()

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                stores.append((i, j))
            elif board[i][j] == 1:
                houses.append((i, j))

    MIN_CITY_CHICK_DISTANCE = 9876543210

    # 치킨집의 총개수에서 M개의 조합을 뽑고 조합마다 치킨거리 계산 후 최솟값 반환

    for selected_store in list(combinations(stores, M)):
        chicken_distacne = list()

        for house in houses:
            house_y, house_x = house[0], house[1]

            MIN_CHICK_DISTANCE = 987654321

            for store in selected_store:
                MIN_CHICK_DISTANCE = min(
                    MIN_CHICK_DISTANCE, get_chick_distance(store[0], store[1], house_y, house_x)
                )

            chicken_distacne.append(MIN_CHICK_DISTANCE)
        MIN_CITY_CHICK_DISTANCE = min(MIN_CITY_CHICK_DISTANCE, sum(chicken_distacne))

    return MIN_CITY_CHICK_DISTANCE


def get_chick_distance(store_y, store_x, house_y, house_x):
    return abs(store_y - house_y) + abs(store_x - house_x)


print(sol())
