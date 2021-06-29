from collections import defaultdict, deque


def solution(n, edge): # T:O(V+E)
    answer = 0
    distance = defaultdict(int)
    adjacency_list=defaultdict(list)
    
    distance[1] = 0
    
    
    for src,dest in edge:
        adjacency_list[src].append(dest)
        adjacency_list[dest].append(src)
    

    def bfs(src, q):
        nonlocal n,adjacency_list, distance
        visit = {src}

        while q:
            node, d = q.popleft()

            

            for neigh in adjacency_list[node]:
                if neigh not in visit:
                    visit.add(neigh)
                    # 처음 방문해보면 거리를 기록
                    distance[neigh]=d+1
                    q.append((neigh,d+1))
    q = deque()
    q.append((1, 0))
    bfs(1, q)

    # distance key 중 value가 가장 큰 값들로 새로운 리스트를 반환
    return len(list(filter(lambda x: distance[x] == max(distance.values()), distance.keys())))