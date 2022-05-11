def solution(n, results):  # T:O(n^2)
    class player:
        def __init__(self, val, win=None, lose=None):
            self.val = val
            # win들에게 이김
            self.win = win or []
            # lose들에게 졌음
            self.lose = lose or []

    players = {i: player(i) for i in range(1, n + 1)}

    answer = 0

    for winner, loser in results:
        players[winner].win.append(players[loser])
        players[loser].lose.append(players[winner])

    def dfs(p, direct, visit):
        visit.add(p.val)
        if direct == "w":
            for winner in p.win:
                if winner.val not in visit:
                    dfs(winner, direct, visit)
        else:
            for loser in p.lose:
                if loser.val not in visit:
                    dfs(loser, direct, visit)

    for num in range(1, n + 1):
        visit = set()

        # 내가 확실하게 이길수 있는 상대들을 dfs로 방문
        dfs(players[num], "w", visit)
        # 내가 무조건 지는 상대들을 dfs로 방문
        dfs(players[num], "l", visit)

        # 만약 나를 제외한 사람들을 모두 방문했다는건
        # 내순위가 정해졌다는 것
        if n == len(visit):
            answer += 1

    return answer
