from sys import stdin

K, N = map(int, stdin.readline().split())


def sol():
    wires = []

    for _ in range(K):
        wires.append(int(stdin.readline()))

    left, right = 1, max(wires)

    answer = 0

    while left <= right:

        mid = (left + right) // 2

        count = 0

        for wire in wires:
            count += wire // mid

        if count >= N:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer


print(sol())
