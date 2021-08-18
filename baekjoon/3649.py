from sys import stdin


def sol(x):
    X = x * 10000000

    n = int(stdin.readline())

    legos = list()

    for _ in range(n):
        legos.append(int(stdin.readline()))

    legos.sort()

    l, r = 0, n - 1

    while l < r:

        s = legos[l] + legos[r]

        if s == X:
            print("yes " + str(legos[l]) + " " + str(legos[r]))
            return
        elif s > X:
            r -= 1
        else:
            l += 1
    print("danger")


while True:
    try:
        x = int(stdin.readline())
        sol(x)
    except:
        break