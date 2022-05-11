from sys import stdin
from collections import deque

V = int(stdin.readline())

# connection[i][j]이 -1이면
# i와 j는 연결되지 않았고
# -1이 아닌 다른 숫자라면 i와 j 사이의 거리를 의미
# connection = [[-1] * (V + 1) for _ in range(V + 1)]

# 인접행렬시 메모리 초과
connection_list = [list() for _ in range(V + 1)]

for i in range(1, V + 1):
    input_list = list(map(int, stdin.readline().split()))
    for dest_idx in range(1, len(input_list), 2):
        if input_list[dest_idx] == -1:
            break
        else:
            # 3 1 2 4 3 -1 이 들어올 경우
            # input_list[dest_idx]는 1,4,-1을 가리킴
            # input_list[dest_idx+1]은 src와 dest 사이의 거리를 의미
            # connection[src][input_list[dest_idx]] = connection[
            # input_list[dest_idx]][src] = input_list[dest_idx + 1]

            # 3 1 2 4 3 -1 이 들어올 경우
            # input_list[dest_idx]는 1,4,-1을 가리킴
            # input_list[dest_idx+1]은 src와 dest 사이의 거리를 의미

            connection_list[input_list[0]].append((input_list[dest_idx], input_list[dest_idx + 1]))


def ans():
    # 트리의 지름은
    # 임의의 정점 v에서 가장 먼 정점 u를 찾고
    # 정점 u에서 가장 먼 정점인 r까지의 거리가 트리의 지름

    # 임의의 정점 1에서
    # 가장 거리가 멀리 떨어진 정점 max_idx 찾기
    check = [False for _ in range(V + 1)]
    check[1] = True
    q = deque()
    q.append((1, 0))

    max_dist = -1
    max_idx = -1

    while q:
        pos, dist = q.popleft()

        for connected_node_info in connection_list[pos]:

            if not check[connected_node_info[0]]:
                q.append((connected_node_info[0], dist + connected_node_info[1]))
                if max_dist < dist + connected_node_info[1]:
                    max_idx = connected_node_info[0]
                    max_dist = dist + connected_node_info[1]
                check[connected_node_info[0]] = True

    # max_idx에서 가장 먼 거리를 찾기
    check = [False for _ in range(V + 1)]
    check[max_idx] = True
    q = deque()
    q.append((max_idx, 0))

    max_dist = -1

    while q:
        pos, dist = q.popleft()

        for connected_node_info in connection_list[pos]:

            if not check[connected_node_info[0]]:
                q.append((connected_node_info[0], dist + connected_node_info[1]))
                max_dist = max(max_dist, dist + connected_node_info[1])
                check[connected_node_info[0]] = True
    print(max_dist)


ans()
