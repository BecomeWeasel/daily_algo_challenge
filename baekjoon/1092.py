from sys import stdin


def sol():
    N = int(stdin.readline())

    cranes = list(map(int, stdin.readline().split()))

    cranes.sort(reverse=True)

    M = int(stdin.readline())

    boxes = list(map(int, stdin.readline().split()))

    boxes.sort(reverse=True)

    t = 0

    if max(boxes) > max(cranes):
        return -1

    while True:
        if len(boxes) == 0:
            break

        for crane in cranes:
            for idx in range(len(boxes)):
                if crane >= boxes[idx]:
                    del boxes[idx]
                    break
        t += 1

    return t


print(sol())
