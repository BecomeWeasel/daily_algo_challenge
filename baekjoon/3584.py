from sys import stdin


class node:
    def __init__(self):
        self.parent = -1

    def set_parent(self, parent):
        self.parent = parent


T = int(stdin.readline())


def ans(N, nodes, first, second):
    firsts_parent = list()

    aim = first

    firsts_parent.append(first)

    while nodes[aim].parent != -1:
        firsts_parent.append(nodes[aim].parent)
        aim = nodes[aim].parent

    aim = second

    while nodes[aim].parent != -1:
        target = nodes[aim].parent

        for parent in firsts_parent:
            if target == parent:
                return target
        aim = target


while T:
    N = int(stdin.readline())
    nodes = [node() for _ in range(N + 1)]
    for i in range(N - 1):
        A, B = map(int, stdin.readline().split())
        nodes[B].set_parent(A)
    first, second = map(int, stdin.readline().split())
    print(ans(N, nodes, first, second))
    T -= 1
