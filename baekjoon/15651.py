from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    visit = [False for _ in range(8 + 1)]

    def dfs(k, nums):
        nonlocal visit
        if k == M:
            print(' '.join(map(str, list(nums))))
            return

        for i in range(1,N+1):
            if not visit[i]:        
                dfs(k+1,nums+str(i))
    
    for i in range(1,N+1):
        dfs(1,str(i))

sol()