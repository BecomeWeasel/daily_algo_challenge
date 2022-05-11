def solution(tickets):
    connections, visited = {}, {}

    for tic in tickets:
        connections[tic[0]] = list()
        visited[tic[0] + tic[1]] = 0

    num_of_tickets = 0

    for tic in tickets:
        # 중복티켓이 있으므로 티켓 방문을 TF가 아닌 개수로 체크
        visited[tic[0] + tic[1]] += 1
        num_of_tickets += 1

        connections[tic[0]].append(tic[1])
        connections[tic[0]].sort()

    result_set = list()

    # 바로 ICN에서 출발
    for next_port in connections["ICN"]:
        tmp = visited.copy()
        tmp["ICN" + next_port] -= 1
        dfs(next_port, 1, num_of_tickets, result_set, tmp, ["ICN", next_port], connections)

    result_set.sort()

    return result_set[0]


def dfs(v, num_of_flight, num_of_tickets, result_set, visited, line, connections):

    # 티켓개수만큼 비행했다면
    if num_of_flight == num_of_tickets:
        result_set.append(line)
        return

    # 새로 도착한 v에서 출발하는 항공편이 없을때
    if not v in connections:
        return

    for next_port in connections[v]:
        if visited[v + next_port] != 0:

            visited[v + next_port] -= 1
            dfs(
                next_port,
                num_of_flight + 1,
                num_of_tickets,
                result_set,
                visited,
                line + [next_port],
                connections,
            )

            # 이 라인 매우 중요
            visited[v + next_port] += 1


solution(
    [
        ["ICN", "BOO"],
        ["ICN", "COO"],
        ["COO", "DOO"],
        ["DOO", "COO"],
        ["BOO", "DOO"],
        ["DOO", "BOO"],
        ["BOO", "ICN"],
        ["COO", "BOO"],
    ]
)
