from sys import stdin

T = int(stdin.readline())


def sol():
    # 예시에서 [4,3,1,2]
    # 왜 A가 4를 가져갔는가?

    # 4를 가져갔다고 해보면, B가 가져갈수 있는 수는 3 혹은 2이다.
    # 이때의 경우에서 A는 양쪽에서 얻는 차가 +1,+2이다. 그 중 가장 차가 적은 건  +1,
    # 이때의 차는 각자의 경우에서 이득치를 의미함.

    # 만약 2를 가져가면, B는 4 혹은 1를 가져갈 수 있다.
    # 이때의 경우에서 A의 양쪽 차는 -2,+1이다. 가장 차가 적은건 -2

    # 그러니 4를 선택했을때의 이득치의 최소가 더 크니 4를 선택

    # 그럼 이제 [3,1,2]다.
    # B가 3을 가져갔다고 해보자.
    # 이럴때 다음 A는 1 혹은 2를 가지고 이때의 이득치의 차이는 +2,+1 인데 이득치가 낮은건 +1

    # 반대로 2를 가져갔다고 해보자.
    # 그러면 A는 3 혹은 1을 가지는데 이득치의 차는 -1,+1 인데 이득치중 낮은건 -1

    # 그러니까 두 경우에서 이득치의 최소가 더 큰 3을 선택..

    # 한번만 더 해보자. [1,2]

    # A가 1을 가져가면 B는 2를 가져가니 이득치는 -1

    # A가 2를 가져가면 B는 1을 가져가니 이득치는 +1

    # 그러니 A는 2를 선택

    # dp로 나타내보자.

    # dp[i] = i 번째 골랐을때 최대 점수라고 하면,
    # dp[i]= dp[i-2] + 왼쪽에서 고르기 or 왼쪽에서 고르기
    # 근데 카드를 고를 수 있는 pool이 달라지니까

    # dp[i][a][b]= a에서 부터 b까지 카드를 고를 수 있을때, i번째 최대 점수
    # dp[i] = max(dp[i-2][a-1][b] + card[],dp[i-2][]
    # 근데 경우의 수 너무많다.

    # 어차피 계산하는건 근우의 점수이다 그럼 근우의 점수가 정해지면, 명우의 점수도 정해짐.
    # 합계에서 빼버리면 되니까..
    # 결국 합계점수가 정해져있다는걸 고려하자


    # dp[a][b] 를 카드가 a~b 번째 카드까지 있을때 근우 A의 점수 최대라고 하면,
    # 근우는 매번 카드 뽑을때 dp 값이 최대인걸 원할거고 (L or R)
    # 명우는 저 값이 최소인걸 원할거임

    # 명우 점수 + 근우 점수 = 합계니까
    # 근우 점수가 낮아야지 지 점수가 커짐.

    # 내가 L에서 고르면 카드 범위는 이제 L+1~R로 축소
    # 내가 R에서 고르면 카드 범위는 이제 L~R-1로 축소
    # 근우 : max(dp[L+1][R]+L,dp[L][R-1]+R)

    # 명우 차례에선 L과 R을 더하면 안됨 , 왜냐면 그 경우는 이미 근우의 수일때 계산되었음
    # 명우 : min(dp[L+1][R],dp[L][R-1])


    

    def dp_helper(d,l,r,count,card):
        # 둘이 어긋나면 고를수 없는 상태임. 그니까 무조건 한쪽만 고를수밖에 없음
        if l>r:
            return 0
        
        if d[l][r]!=-1:
            return d[l][r]

        # 이때는 근우 차례
        if count%2==0:
            d[l][r]=max(dp_helper(d,l+1,r,count+1,card)+card[l],dp_helper(d,l,r-1,count+1,card)+card[r])
            return dp[l][r]
        # 이때는 명우 차례
        else:
            d[l][r]=min(dp_helper(d,l+1,r,count+1,card),dp_helper(d,l,r-1,count+1,card))
            return dp[l][r]


    answer = 0

    N = int(stdin.readline())

    cards = list(map(int, stdin.readline().split()))


    dp=[[-1 for _ in range(len(cards))] for _ in range(len(cards))]

    dp_helper(dp,0,N-1,0,cards)

    return dp[0][N-1]

while T > 0:
    print(sol())
    T -= 1
