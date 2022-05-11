from sys import stdin
import math

K = int(stdin.readline())


def sol():
    print(int(math.pow(2, K)) - 1)

    def move(a, b, n):
        if n == 1:
            print(" ".join(map(str, [a, b])))
            return
        move(a, 6 - a - b, n - 1)
        print(" ".join(map(str, [a, b])))
        move(6 - a - b, b, n - 1)

    move(1, 3, K)


sol()
