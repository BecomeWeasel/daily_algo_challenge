from collections import defaultdict
from sys import stdin,stdout

def sol():
    N=int(stdin.readline())

    M=int(stdin.readline())

    needs=defaultdict(list)


    # 두 중간 부품이 서로를 필요로 하는 경우가 없다.
    # 이 말은 뭐냐  그니까 서로를 필요로 하지 않기 때문에
    # 발전소처럼 서로가 의존하는 경우는 없음
    # 그말은 중간 부품이 아무리 있다해도,
    # 순서가 명확히 정해져있다는 거임

    graph=[[0 for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        x,y,k=map(int,stdin.readline().split())

        needs[x].append((y,k))

        graph[x][y]=1



    # 그럼 순서가 정해져있고, 먼저 끝내야하는것대로 계산해야하니
    # 바로 생각드는건 위상정렬임.
    # 그럼 indegree가 0인건 명확함 
    # needs에 안들어있는게 일단은 0임.
    # needs는 일종의 계산대기열이라고 생각하자.
    # 그럼 매번 0이된걸 체크할수 없으니
    # 큐하나 만들어서 indegree가 0이 된걸 추적하자
    # zero_indegree=[x for x in range(1,N+1) if x not in needs.keys()]

    dp=[defaultdict(int) for _ in range(N+1)]

    # visit=[False for _ in range(N+1)]

    # order=[]

    # while len(zero_indegree)>0:

    #     for e in zero_indegree:
    #         visit[e]=True
    #         for i in range(1,N+1):
    #             graph[i][e]=0
    #         order.append(e)
    #     zero_indegree=[x for x in range(1,N+1) if not visit[x] and sum(graph[x])==0]
    
    # 이제 order의 순서대로 dp 계산하면 됨.
    # 그럼 6을 계산할때 5는 이미 계산되어 있음
    # 다시말해서 중간부품 Y를 계산할때 필요한 X의 부품은 계산되어 있음

    def calc(num):
        # 이게 리프일때

        if dp[num]:
            return dp[num]

        if num not in needs.keys():
            dp[num][num]=1
            return dp[num]
        else:
            need=needs[num]
            # K번 부품을 완성하는데 필요한 부품은
            # gear번이 amount개가 필요함
            
            # gear번이 완성되는데 또 필요한건
            # basic 기본부품이 c개 만큼 필요함
            for gear,amount in need:
                for basic,c in calc(gear).items():
                    dp[num][basic]+=c*amount
            
            return dp[num]

    # 근데 위상정렬자체가 필요가 없을수도
    # 어차피 순서뒤바뀌어도 
    # 예를 들어서 6먼저 계산하면, 5는 나중에 다시 계산안해도 되니까
    calc(N)
    
    for k,v in sorted(dp[N].items()):
        print(k,v)

sol()

        
