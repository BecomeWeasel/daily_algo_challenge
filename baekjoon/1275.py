from sys import stdin

N, Q = map(int, stdin.readline().split())
tree = [0 for _ in range(N * 4)]
arr = list(map(int, stdin.readline().split()))


def init(node, start, end):
    global arr, tree
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2

    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)

    return tree[node]


def update(node, start, end, index, diff):
    global arr, tree

    # 바꾸려는 값이 범위를 벗어났다면
    # -> 바꿔도 구간합 start-end 사이에는 영향이 없을때
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


def partial_sum(node, start, end, left, right):
    global arr, tree

    # 구하려는 arr[l-r]이 아예 범위 바깥일때
    if left > end or right < start:
        return 0
    # arr[l-r]이 start와 end 구간을 완전포함하고 있을때
    elif left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return partial_sum(node * 2, start, mid, left, right) + partial_sum(
        node * 2 + 1, mid + 1, end, left, right
    )


def sol():
    global arr, tree

    init(1, 0, N - 1)

    # print(tree)
    # # arr[2]을 11으로 변경할것
    # # 3->11로 변경
    # # 총 구간합은 8이 늘어남
    # update(tree,1,0,N-1,2,8)

    for _ in range(Q):
        x, y, a, b = map(int, stdin.readline().split())

        if x > y:
            x, y = y, x

        print(partial_sum(1, 0, N - 1, x - 1, y - 1))
        update(1, 0, N - 1, a - 1, b - arr[a - 1])
        arr[a - 1] = b


sol()
