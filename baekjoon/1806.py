from sys import stdin


def sol():
    N, S = map(int, stdin.readline().split())

    numbers = list(map(int, stdin.readline().split()))

    s, e = 0, 0

    answer = float('inf')

    tot = numbers[s]

    while e < N:
        if tot < S:
            e += 1
            if e == N:
                break
            tot += numbers[e]
        else:
            answer = min(answer, e - s + 1)
            tot -= numbers[s]
            s += 1

    return answer if answer != float('inf') else 0


print(sol())
