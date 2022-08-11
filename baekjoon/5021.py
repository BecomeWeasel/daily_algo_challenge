from sys import stdin
from collections import defaultdict

N, M = map(int, stdin.readline().split())


blood = defaultdict(int)

king = stdin.readline().strip()

count_set = set()

parent = {}

for _ in range(N):
    child, p1, p2 = stdin.readline().strip().split()
    count_set.add(child)
    count_set.add(p1)
    count_set.add(p2)
    parent[child] = list()
    parent[child].append(p1)
    parent[child].append(p2)

node_count = len(count_set)

blood[king] = 1 << node_count


def dfs(name):
    # 도달점
    if name == king:
        return blood[king]

    if blood[name] != 0:
        return blood[name]

    # 평민출신
    if name not in parent:
        return 0

    blood[name] = 0

    for p in parent[name]:
        blood[name] += dfs(p) >> 1

    return blood[name]


answer = (0, "")

for _ in range(M):
    name = stdin.readline().strip()
    ret = dfs(name)

    if ret > answer[0]:
        answer = (ret, name)

print(answer[1])
