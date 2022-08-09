from sys import stdin, setrecursionlimit

setrecursionlimit(3 * 10**6)


K = int(stdin.readline())

weight = list(map(int, stdin.readline().split()))

N = len(weight) + 1

weight.insert(0, 0)
weight.insert(0, 0)
# 루트가 1부터 시작하게끔

to_leaf = [0 for _ in range(2 ** (K + 1) + 1)]


def longest_path(node, dist):
    global longest_path_weight, to_leaf
    to_leaf[node] = dist

    if node * 2 <= N:
        longest_path(node * 2, dist + weight[node * 2])
        longest_path(node * 2 + 1, dist + weight[node * 2 + 1])


longest_path(1, 0)

longest_path_weight = max(to_leaf)

change = [0 for _ in range(2 ** (K + 1) + 1)]
differ = [0 for _ in range(2 ** (K + 1) + 1)]


def push_down(node, total):
    global change

    if node > N:
        return

    differ[node] = change[node] - total

    push_down(node * 2, total + differ[node])
    push_down(node * 2 + 1, total + differ[node])


# print(N)
def up(node):
    global change

    if node == 1 and N >= 3:
        left_need = up(node * 2)  # 999
        right_need = up(node * 2 + 1)  # 0
        push_down(node * 2, 0)
        push_down(node * 2 + 1, 0)

    # 브랜치 노드일때
    elif node * 2 <= N:
        left_need = up(node * 2)
        right_need = up(node * 2 + 1)
        change[node] = min(left_need, right_need)
        return min(left_need, right_need)
    else:
        # 리프노드일때
        change[node] = longest_path_weight - to_leaf[node]
        return longest_path_weight - to_leaf[node]


up(1)

print(sum(differ) + sum(weight))
