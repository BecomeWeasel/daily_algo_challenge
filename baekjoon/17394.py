from sys import stdin
from collections import deque

T = int(stdin.readline())


def ans(N, A, B, candidate_prime):

    q = deque()
    q.append((N, 0))
    check = set()
    check.add(N)

    # 바로 소수가 되었다면
    if N in candidate_prime:
        return 0

    while q:
        num, time = q.popleft()

        for new_num in int(num / 2), int(num / 3), num - 1, num + 1:

            # if new_num > 100000 or new_num < 2:
            #   continue

            if not new_num in check:
                if new_num in candidate_prime:

                    return time + 1
                else:
                    q.append((new_num, time + 1))
                    check.add(new_num)

    return -1


while T:
    N, A, B = map(int, stdin.readline().split())

    is_prime = [True for _ in range(B + 1)]

    # A부터 B까지의 존재하는 소수만 구하면 됨
    m = int(B**0.5)

    for i in range(2, m + 1):
        if is_prime[i] == True:
            for j in range(i * 2, B + 1, i):
                is_prime[j] = False

    # A 이상 B 이하 소수들의 집합
    candidate_prime = set()

    for i in range(A, B + 1):
        # A 이상 B 이하 소수들을 집합에 추가함
        if is_prime[i]:
            candidate_prime.add(i)

    # A 이상 B 이하 소수가 1개도 없으면 -1 출력
    print(len(candidate_prime) == 0 and -1 or ans(N, A, B, candidate_prime))

    T -= 1
