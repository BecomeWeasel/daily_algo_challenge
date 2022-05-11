from sys import stdin

N = int(stdin.readline())


def sol():
    global N

    return "SK" if N % 2 != 0 else "CY"


print(sol())
