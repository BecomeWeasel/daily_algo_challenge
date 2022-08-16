from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

numbers = []

for _ in range(N):
    numbers.append(int(stdin.readline()))

max_seg_tree = [0 for _ in range(N * 4)]
min_seg_tree = [0 for _ in range(N * 4)]


def init_max(numbers, left, right, node):
    global max_seg_tree
    if left == right:
        max_seg_tree[node] = numbers[left]
        return max_seg_tree[node]

    mid = (left + right) // 2

    max_seg_tree[node] = max(
        init_max(numbers, left, mid, node * 2), init_max(numbers, mid + 1, right, node * 2 + 1)
    )

    return max_seg_tree[node]


def init_min(numbers, left, right, node):
    global min_seg_tree
    if left == right:
        min_seg_tree[node] = numbers[left]
        return min_seg_tree[node]

    mid = (left + right) // 2

    min_seg_tree[node] = min(
        init_min(numbers, left, mid, node * 2), init_min(numbers, mid + 1, right, node * 2 + 1)
    )

    return min_seg_tree[node]


def query_max(start, end, node, node_left, node_right):
    if start > node_right or end < node_left:
        return -1

    if start <= node_left and end >= node_right:
        return max_seg_tree[node]

    mid = (node_left + node_right) // 2

    return max(
        query_max(start, end, node * 2, node_left, mid),
        query_max(start, end, node * 2 + 1, mid + 1, node_right),
    )


def query_min(start, end, node, node_left, node_right):
    if start > node_right or end < node_left:
        return float("inf")

    if start <= node_left and end >= node_right:
        return min_seg_tree[node]

    mid = (node_left + node_right) // 2

    return min(
        query_min(start, end, node * 2, node_left, mid),
        query_min(start, end, node * 2 + 1, mid + 1, node_right),
    )


init_max(numbers, 0, N - 1, 1)
init_min(numbers, 0, N - 1, 1)


for _ in range(M):
    a, b = map(int, stdin.readline().split())
    m = query_min(a - 1, b - 1, 1, 0, N - 1)
    M = query_max(a - 1, b - 1, 1, 0, N - 1)
    stdout.write(f"{m} {M}\n")
