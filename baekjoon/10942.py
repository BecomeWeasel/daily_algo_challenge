from sys import stdin, stdout


def sol():
    N = int(stdin.readline())

    numbers = list(map(int, stdin.readline().split()))

    M = int(stdin.readline())

    answer = [[-1 for _ in range(N)] for _ in range(N)]

    query = []

    for _ in range(M):
        S, E = map(int, stdin.readline().split())
        query.append((S, E))

    # 가운데 쪼개서 하는건 반례가 너무많아

    # 1 2 3 4 3 2 1

    # 가운데 쪼개면 펠린드롬아님
    # 근데 합쳐지면 펠린드롬임
    # 에헤이

    # 그럼 이건 어떰?

    # 		S               X                E 라고했을때

    # 가운데 중간지점 아무데나 잡으셈 홀수라고하면 거길 X라고 해보자

    # 이랬을때 [X,X]는 무조건 펠린드롬임
    # 그럼  [X-1,X+1]은? 그말은 X-1과 X+1이 같아야지 펠린드롬의 구간을 확장할수 있음.

    # X를 기준으로 봤을때 좌우대칭이여야함 그니까 가운데 하나를 잡고 계속 확장한다 생각해보자.
    # X는 항상 펠린드롬인때 양끝에 공평하게 같은 수를 계속 붙여나가는거임
    # 1 X 1 -> 2 1 X 1 2 -> 3 2 1 X 1 2 3
    # 그럼 항상 펠린드롬 아님? ㅇㅇ 맞지

    # 반대로 [i,j]가 펠린드롬이라고 해보자. 양 끝에 같은 수 X를 붙이자 .

    # X [i~~j] X -> 이거 무조건 펠린드롬임.

    # 그럼 반대로 [i,j]가 대칭이려면, [i+1,j-1]도 대칭이여야함.

    # 뭔말이냐면 i번째와 J번째를 추가된 원소라고 보는거임
    # 그러면 i번째 수와 J번째 수는 무조건 같아야하고,
    # [i+1,j-1] 원소는 이미 펠린드롬을 갖춘 상태라는거임
    #               i+1 ..... j-1
    # 이게 펠린드롬일때
    #           i i+1 ...... j-1  j
    # i와 j를 양끝에 붙여서 펠린드롬이려면 당연히 i와 J는 같아야하는거니까

    # [i,j] 계산 방법은 당연히 num(i),num(j)같고 , [i+1,j-1]도 대칭이여야함

    # dp[i][j]= num(i) == num(j) && dp[i+1][j-1]

    # [i,j]가 펠린드롬이려면 , 그 서브구간도 당연히 펠린드롬이여야한다는 원칙으로 가니까 재귀로 풀자

    # 1 2 2 1 같은 짝수는? 내풀이가 홀수일때만 되나?

    # 이때도 같을거같은데

    # [1,4]가 펠린드롬이려면, num(1)==num(4)이여야 하고  [2,3]도 펠린드롬이여야함

    # 만약 i==j같으면 무조건 성공

    # 두개가 어긋날수 있을까?

    # [2 , 5] 검사 하면 num(2)==num(5) 할거고 [3,4] 비교

    # num(3) == num(4) 할거고 [4,3] 비교 ㅇㅋ 이거 엇갈리네
    # 근데 엇갈리면 검토할필요가 없음 왜냐면 num(3)==num(4)검사한순간 이미 펠린드롬 확정임
    # 그니까 i가 j보다 크면 무조건 펠린드롬이라는 1 반환

    def cal(i, j, dp, nums):
        # print(i,j)
        # 어긋나면 무조건 1
        # 왜냐면 어긋낫다는건 i-1,j+1이 딱 1차이 난다는거고 한칸차이면 비교 할필요가 없음
        if i > j:
            return 1
        # 이미 계산되어있다면
        if dp[i][j] != -1:
            return dp[i][j]
        # 만약 [3,3] 이면 이건 길이 1인 펠린드롬인거지
        # if i == j:
        #     dp[i][j] = 1
        #     return dp[i][j]
        else:
            # num(i)와 num(j)가 같다는건 [i-1,j+1]에 i와 j를 추가한 상황이라고 보자.
            # 그럼 i와 j말고 [i-1,j+1] 구간만 검사하자
            if nums[i] == nums[j] and cal(i + 1, j - 1, dp, nums):
                dp[i][j] = 1
                return dp[i][j]
            # 두 조건중에 하나라도 어긋나면 펠린드롬 절대안됨
            # [i-1,j+1] 구간에 양 끝에 서로 다른값 추가한거니까
            # 또 끝이 서로 같아도 가운데 구간이 틀리면 X
            else:
                dp[i][j] = 0
                return 0

    for i in range(N):
        answer[i][i] = 1

    for s, e in query:
        stdout.write(str(cal(s - 1, e - 1, answer, numbers)) + "\n")
        # print(ret)


sol()
