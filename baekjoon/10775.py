from sys import stdin


def find_parent(x, parent):
    if parent[x] == x:
        return x
    P = find_parent(parent[x], parent)
    parent[x] = P
    return parent[x]


def union(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def sol():

    G = int(stdin.readline())
    P = int(stdin.readline())

    parent_table = {k: k for k in range(G + 1)}
    ans = 0

    # parent_table[i] !=i 면 연결된 상태
    # i면 아직 연결안된 상태

    fly = []

    for _ in range(P):
        fly.append(int(stdin.readline()))

    for f in fly:
        p = find_parent(f, parent_table)

        if p == 0:
            return ans

        union(p, p - 1, parent_table)
        ans += 1
    return ans


print(sol())
