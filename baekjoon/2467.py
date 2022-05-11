from sys import stdin

N = int(stdin.readline())


def sol():
    liquid = list(map(int, stdin.readline().split()))

    l, r = 0, len(liquid) - 1

    abs_value = abs(liquid[l] + liquid[r])
    sol1, sol2 = liquid[l], liquid[r]

    while l < r:
        mix_value = liquid[l] + liquid[r]

        if abs(mix_value) < abs_value:
            sol1, sol2 = liquid[l], liquid[r]
            abs_value = abs(mix_value)

        if mix_value > 0:
            r -= 1
        elif mix_value < 0:
            l += 1
        else:
            break

    print(" ".join(map(str, [sol1, sol2])))


sol()
