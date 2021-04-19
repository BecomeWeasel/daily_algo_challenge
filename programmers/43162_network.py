from collections import deque


def bfs(q, visit, connection):
    while len(q) != 0:
        front = q.popleft()

        for idx, is_connected in enumerate(connection[front]):
            if is_connected and not visit[idx]:
                q.append(idx)
                visit[idx] = True


def solution(n, computers):
    answer = 0
    connection = computers
    visit = [False for _ in range(n)]
    for node in range(n):

        if not visit[node]:
            visit[node] = True
            answer += 1
            q = deque()
            q.append(node)
            bfs(q, visit, connection)

    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
