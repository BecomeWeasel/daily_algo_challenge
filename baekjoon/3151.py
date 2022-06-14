from sys import stdin
from bisect import bisect_left, bisect_right

N = int(stdin.readline())


def sol():
    numbers = list(map(int, stdin.readline().split()))

    # 1<=N<=10000
    # 그냥 단순 two sum 문제면 루프만 돌려도 됨.
    # 근데 이건 세개이고, N^3으론 해결이 안됨.
    # (a,b,c) 순서쌍에 대하여 (a!=b!=c)
    # numbers[a]+numbers[b]+numbers[c]=0을 만족하는것을 찾아야 함.

    # 그럼 반대로 numbers[a]+numbers[b]=-numbers[c]
    # 인데 중복도 있으니 단순 해결은 안됨.

    # N^2으로 줄여야하는데................................................................

    # 숫자들의 위치는 중요하지 않음.
    # 그냥 정렬해서 원하는 숫자인 numbers[c]를 찾을때 이분탐색을 이용하자.
    # 대신에 같은 사람이 두번 선택되면 안되니까 이건 기록해야함.

    sorted_numbers = sorted(numbers)

    numbers_set = set(sorted_numbers)

    answer = 0

    for i in range(N):
        for j in range(i + 1, N):
            c = -(sorted_numbers[i] + sorted_numbers[j])

            if c in numbers_set:
                # 중복 무시하면서 개수세기
                answer += bisect_right(sorted_numbers, c, j + 1, N) - bisect_left(
                    sorted_numbers,
                    c,
                    j + 1,
                )

    return answer


print(sol())
