def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0
    parent = [0] * n
    num_of_connected_island = 0

    for i in range(n):
        parent[i] = i

    # MST를 구성해야하니
    # kruskal 이용하기 위해서 다리의 cost가 낮은 순서대로 정렬
    costs.sort(key=lambda x: x[2])

    for cost in costs:
        # n개의 섬이 모두 한 집합안에 있다면
        # n개의 섬이 모두 연결된 것
        if num_of_connected_island == n:
            break
        # 섬끼리 같은 집합이 아니라면 union 해야함
        if find_parent(parent, cost[0]) != find_parent(parent, cost[1]):
            union_parent(parent, cost[0], cost[1])
            answer += cost[2]
            num_of_connected_island += 1
        else:
            continue

    print(costs)

    return answer
