from sys import stdin, setrecursionlimit

T = int(stdin.readline())
setrecursionlimit(200000)


def sol():
    n = int(stdin.readline())

    connect = list(map(int, stdin.readline().split()))

    team=[]

    visited=[False for _ in range(n)]

    def dfs(node,t):
        nonlocal team
        visited[node-1]=True

        next_node=connect[node-1]
        
        if not visited[next_node-1]:
            t.append(next_node)
            dfs(next_node,t)
        else:
            if next_node in t:
                for m in t[t.index(next_node):]:
                    team.append(m)
                # print(team)

    for i in range(1,n+1):
        if not visited[i-1]:
            dfs(i,[i])
    
    return n-len(team)


for _ in range(T):
    print(sol())