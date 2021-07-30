from sys import stdin, setrecursionlimit
from collections import deque, defaultdict

T = int(stdin.readline())

setrecursionlimit(110000)


def sol():
    N, M = map(int, stdin.readline().split())

    indegree = [0 for _ in range(100001)]

    indegree[0] = float('inf')

    edges = defaultdict(list)

    for _ in range(M):  # O(E)
        src, dest = map(int, stdin.readline().split())
        edges[src].append(dest)
        indegree[dest] += 1

    visit = set()

    def bfs(node):
        nonlocal visit

        q = deque()
        q.append(node)
        visit.add(node)

        while q:
            v = q.popleft()
            for neigbors in edges[v]:
                if neigbors not in visit:
                    visit.add(neigbors)
                    q.append(neigbors)

    steps = 0

    # indegree가 0인애들은 무조건 넘겨뜨려야함 O(V)
    for node in range(1, N + 1):
        if indegree[node] == 0:
            steps += 1
            bfs(node)

    reversed_edges = defaultdict(list)

    # 코사라주 위해서 edge 모두 뒤집기
    for key in edges.keys():
        for t in edges[key]:
            reversed_edges[t].append(key)

    SCC_count = 0
    end_dfs_stack = []
    scc_visit = set()

    def dfs(node):
        nonlocal visit, end_dfs_stack
        visit.add(node)

        for neighbor in edges[node]:
            if neighbor not in visit:
                dfs(neighbor)

        end_dfs_stack.append(node)

    def reversed_dfs(node, scc: list):
        nonlocal scc_visit, reversed_edges
        scc.append(node)
        visit.add(node)

        for neighbor in reversed_edges[node]:
            if neighbor not in visit:
                reversed_dfs(neighbor, scc)

    # 코사라주 정방향 dfs
    for node in range(1, N + 1):
        # SCC 파악하기
        if node not in visit:
            dfs(node)

    visit = set()
    # scc들이 모여있음
    total_scc = []

    # 코사라주 역방향 dfs
    while end_dfs_stack:
        scc = []
        v = end_dfs_stack.pop()

        if v in visit:
            continue

        reversed_dfs(v, scc)
        total_scc.append(scc)

    scc_indicator = defaultdict(lambda: -1)
    scc_indegree = defaultdict(lambda: 0)

    # 각 노드들에 SCC 번호 붙여주기
    for scc_num in range(len(total_scc)):  # O(V)
        for element in total_scc[scc_num]:
            scc_indicator[element] = scc_num + 1

    for scc_num in range(len(total_scc)):  # O(E)
        for element in total_scc[scc_num]:
            for r_edge in reversed_edges[element]:
                # 다른 scc에서 온 edge이면
                # scc indegree가 1 늘어남
                if scc_indicator[r_edge] > 0 and scc_indicator[r_edge] != scc_num + 1:
                    scc_indegree[scc_num] += 1

    # 총 scc의 개수에서 scc_indegree가 0이상인 scc의 개수를 빼면
    # 추가적으로 넘어뜨려야할 scc 개수 구할수 있음
    num_indegree_zero_scc = len(total_scc) - len(scc_indegree.keys())

    return steps + num_indegree_zero_scc


for _ in range(T):
    print(sol())