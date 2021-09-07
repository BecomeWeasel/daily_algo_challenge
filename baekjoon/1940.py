from sys import stdin


def sol():
    N = int(stdin.readline())
    M = int(stdin.readline())
    answer = 0
    numbers = list(map(int, stdin.readline().split()))

    numbers.sort()

    l, r = 0, N - 1

    while l != r:
        s = numbers[l] + numbers[r]

        if s == M:
            answer += 1
            l += 1
        elif s < M:
            l += 1
        else:
            r -= 1

    return answer


print(sol())
