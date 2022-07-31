from sys import stdin
import heapq as hq
from collections import defaultdict

N, M = map(int, stdin.readline().split())

edges = [defaultdict(int) for _ in range(N + 1)]

# 문제 아이디어 자체는 쉬움

# 음주단속 하는 곳이라고 생각해보면, 원래 루트에서 음주단속안하면 이건 걱정할거없잔아요.....

# 다시말하면 원래 루트를 막고, 그럼 다른 우회로를 찾고 ... 이 과정 반복임

# 시간복잡도 때문에 많이 쫄았는데 생각해보면 너무 자명하게 풀린다.
# E 들 가운데서 최단 경로를 구성하는 E들을 Es, 아닌 엣지들을 El이라고 할때,
# E= Es+ El <=5000
# 그러면 시간복잡도는 Es*ElogV이다.

# 가장 길어질때는 그러면 Es가 클때, 다시말해서 Es~=E일때인데,
# 이때는 E^2 log V인데 , 계산해보면 5000*5000*log1000이니까 2억5천
# 안될거같지만, 만약 Es=E이면, ElogV 한번에 끝난다. -1 나오고 끝이니 ...

# 반대로 El>>>>>>>Es일경우, 예를 들어 극단적으로 Es=10 El=4990
# 10*5000*log1000=10*5000*10=50만 무조건됨.

# 그럼 Es=El일때는,
# 2500*5000*10=1억2천5백만 ... 터지는거같이 보이는데 ... 잘생각해보면
# Es는 무조건 N이하다.
# 생각해보면, 최단거리를 하기 위해서는 재방문할필요가 없다.
# 즉 Es가 아무리커도 E까지는 절대 못간다. 최대 N이니
# Es<=N<=1000 < E <=5000
# 그러니 시간복잡도는 EVlogV니 1000*5000*10=5천만

for _ in range(M):
    a, b, t = map(int, stdin.readline().split())

    edges[a][b] = t
    edges[b][a] = t

dist = [1e10 for _ in range(N + 1)]

prev = [-1 for _ in range(N + 1)]

pq = []

pq.append((0, 1))

dist[1] = 0

while pq:
    current_dist, current_node = hq.heappop(pq)

    if dist[current_node] < current_dist:
        continue

    for new_node, new_dist in edges[current_node].items():
        distance = current_dist + new_dist

        if distance < dist[new_node]:
            dist[new_node] = distance
            prev[new_node] = current_node
            hq.heappush(pq, (distance, new_node))

origin_min_distance = dist[N]

s_path = []
dest = N
while dest != -1:
    # print(dest)
    s_path.append((dest, prev[dest]))
    dest = prev[dest]

s_path.pop()

answer = -1

for src, dest in s_path:
    origin_value = edges[src][dest]

    edges[src][dest] = edges[dest][src] = 1e10

    dist = [1e10 for _ in range(N + 1)]

    pq = []

    pq.append((0, 1))

    dist[1] = 0

    while pq:
        current_dist, current_node = hq.heappop(pq)

        if dist[current_node] < current_dist:
            continue

        for new_node, new_dist in edges[current_node].items():
            distance = current_dist + new_dist

            if distance < dist[new_node]:
                dist[new_node] = distance
                prev[new_node] = current_node
                hq.heappush(pq, (distance, new_node))

    if dist[N] == 1e10:
        answer = -1
        break
    else:
        answer = max(answer, abs(dist[N] - origin_min_distance))

    edges[src][dest] = edges[dest][src] = origin_value


print(answer)
