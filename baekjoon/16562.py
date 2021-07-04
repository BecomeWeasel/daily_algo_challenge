from sys import stdin


def sol():
    N,M,K=map(int,stdin.readline().split())
    friend_cost=list(map(int,stdin.readline().split()))

    costs=list()
    # kruskal인데 0하고 연결되어 있는 가격만 나옴
    # 비용 적은 순서대로 추가
    for i in range(N):
        costs.append((friend_cost[i],i+1)) 
    costs.sort()

    # 처음엔 bfs 쓰려했는데 MST니까 kruskal

    # 0번이 준석이
    parent=[i for i in range(N+1)]

    def find(X):
        nonlocal parent

        if parent[X]!=X:
            return find(parent[X])
        else:
            return X
    
    def union(X,Y):
        X=find(X)
        Y=find(Y)

        if X<Y:
            parent[Y]=X
        else:
            parent[X]=Y
    
    # 각각의 친구 관계에 대해서
    # a,b를 같은 친구집합으로 합쳐줌
    for _ in range(M):
        a,b=map(int,stdin.readline().split())
        union(a,b)
    
    answer=0
    for cost_tuple in costs:
        cost,num=cost_tuple
        # 준석이와 num번 친구가 
        # 서로 아직 친구관계가 아니라면
        if find(0)!=find(num):
            answer+=cost
            union(0,num)
        # 이미 친구 관계라면 ('친구의 친구는 친구다'로 인해서)
        # 그냥 pass
    
    # MST 구축 최소 비용이 K원 보다 많이 들면 구성 불가
    return answer if answer<=K else "Oh no"

print(sol())