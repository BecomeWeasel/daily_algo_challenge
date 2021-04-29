from sys import stdin

N, C = map(int, stdin.readline().split())


def sol():
    answer = 0
    houses = []
    for _ in range(N):
        houses.append(int(stdin.readline()))

    houses.sort()

    left, right = 1, max(houses) - min(houses)

    while left <= right:
        max_distance = (left + right) // 2

        prev=houses[0]

        router_cnt = 1

        for idx in range(1, len(houses)):
            if houses[idx] - prev >= max_distance:
                router_cnt += 1
                prev=houses[idx]

        if router_cnt >= C:
            left = max_distance + 1
            answer = max(answer, max_distance)
        else:
            right = max_distance - 1

    return answer


print(sol())