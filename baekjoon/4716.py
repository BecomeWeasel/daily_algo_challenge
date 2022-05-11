import bdb
from sys import stdin

# 3 15 35
# 10 20 10 1 차 : 10
# 10 10 30 2 차 : 20
# 10 40 10 3 차 : 30
# 0 0 0

# -> 300

# 어차피 풍선은 다 주긴 해야됨.
# 그러면 차이가 큰 사람 vs 차이는 적게 나는데 애초에 코스트가 높은사람
# 누가먼저 받을지 결정
# 10 80 vs 990 1000
# 어차피 다 줄거 차이 크게 나는 앞사람 먼저 주자

# 아니다 반대로 차이가 적게나는애는 뭘 받아고 괜찮을거야
# 차이가 크게 나는애 먼저 지 원하는거 받게 해주자

# 위 얘시에서 차이가 큰 순서대로 먼저 정렬하면
# 3->2->1
# 3 먼저 줘보자.
# 그럼 풍선은 15 25 남고
# ans+= 10 * 10
# 2 주면
# 5 25 남고
# ans+= 10 * 10
# 1 주면
# 5 15 남고
# ans+= 10 * 10

# 차이가 큰 순서대로 정렬했을때 그리고 A가 엄청 많다고 해보자 B에 비해서
# 어떤애는 차이가 엄청 크면,

# 차이그 큰 순서대로 정렬했을때, 차이가 같으면 애초에 숫자가 작은애 먼저 배정받아야 하나?
# 10 110 vs 1000 1100
# 둘다 100 차이 나는데 근데 만약 원하는 풍선이 같으면 문제 X 순서 상관 X
# 근데 전자는 풍선 10000개 원하고 후자는 1개 원하면
# 풍선 개수 * 차이에 비례해서 코스트가 커진다

# 전자 먼저 주나? 전자가 풍선 다 가져가면 후자는 무조건 지켜봐야하는데
# 만약에 풍선 원하는 숫자를 작은 순서먼저 준다고 해보자
# 그럼 뒤에서 10000개 다 온전히 가져갈거 (차이 적은 값으로)
# 9000개만 차이 큰걸로 가져갈수도 있다 그럼 손해가 큼.
# 그니까 원하는 풍선 개수 큰사람 먼저

# 근데 간단한 문제가 아닌게 결국에 최악은 k*diff 만큼 차이가 나니까 이 임팩트가 큰 순서대로? -> 근데 이거 틀림
# 근데 그 임팩트가 같다면 ?
# 1 10 110 vs 10 90 100

# 1 * 100 vs 10 * 10 똑같네?

# A B 다른게 좀 걸리는데..

# 만약에 차이가 같다면? 1000 990 vs 20 10
# 상관없을거같은데
# 근데 차이가 같은데 990 1000 vs 20 10
# 이럴땐 정렬 잘해야될수도, 원하는 위치가 다르니까
# 만약에 B 풍선이 더많다고 해보자.
# 그럼 A에 대해서 더 경쟁이 일어날거같으니까
# A 먼저 배치할까


# 정렬을 A에 가까운 순서대로 정렬, B에 가까운 순서대로 정렬
# A 정렬
# 2 < 1 < 3

# B 정렬
# 1,3 < 2


def sol(n, a, b):
    N, A, B = n, a, b
    teams = []
    answer = 0
    for _ in range(N):
        k, a_d, b_d = map(int, stdin.readline().split())
        teams.append((k, a_d, b_d))

    # # A 풍선이 더 많으면,  고려해야하나
    # if A>=B:
    #     teams.sort(key=lambda x:(-abs(x[2]-x[3]),x[2]))
    # else:
    #     teams.sort(key=lambda x:(-abs(x[2]-x[3]),x[3]))
    # teams.sort(key=lambda x: (-abs(x[2]-x[3]),-x[1]))

    # 이건 틀렸고
    # teams.sort(key=lambda x: (-abs(x[1]-x[2])*x[0]))
    # 이건가 ? 풍선 만개 받는애 차이가 1나면, 사실 그게그건데
    # 얘가 9999 차이나는 1개 원하는애보다 먼저 올 수 있으니?

    # 이건 맞음
    teams.sort(key=lambda x: (-abs(x[1] - x[2])))

    # for r in teams:
    #     print(r)

    # 이 아랫부분은 정상적임.
    for team in teams:
        ballon, a_d, b_d = team

        # 이 팀은 A에서 받고 싶음
        if a_d <= b_d:
            if A >= ballon:
                A -= ballon
                answer += ballon * a_d
            else:
                answer += A * a_d
                ballon = ballon - A
                A = 0
                B -= ballon
                answer += ballon * b_d
        # 얘넨 B에서 받고싶대
        else:
            if B >= ballon:
                B -= ballon
                answer += ballon * b_d
            else:
                answer += B * b_d
                ballon = ballon - B
                B = 0
                A -= ballon
                answer += ballon * a_d

    return answer


while True:
    N, A, B = map(int, stdin.readline().split())

    if N == A == B == 0:
        break

    print(sol(N, A, B))
