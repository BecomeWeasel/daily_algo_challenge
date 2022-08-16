from sys import stdin


N, M = map(int, stdin.readline().split())

ads = list(map(int, stdin.readline().split()))

seg_tree = [0 for _ in range(N * 4)]


def init(arr, l, r, node):
    global seg_tree
    if l == r:
        seg_tree[node] = arr[l]
    else:
        mid = (l + r) // 2

        seg_tree[node] = max(init(arr, l, mid, node * 2), init(arr, mid + 1, r, node * 2 + 1))
    return seg_tree[node]


init(ads, 0, N - 1, 1)

# print(seg_tree)


def query(s, e, node, node_left, node_right):
    if s > node_right or e < node_left:
        return -1

    if s <= node_left and e >= node_right:
        return seg_tree[node]

    mid = (node_left + node_right) // 2

    return max(
        query(s, e, node * 2, node_left, mid), query(s, e, node * 2 + 1, mid + 1, node_right)
    )


answer = []

for c in range(M - 1, N - M + 1 - 1 + 1):
    answer.append(query(c - (M - 1), c + (M - 1), 1, 0, N - 1))

print(" ".join(map(str, answer)))
