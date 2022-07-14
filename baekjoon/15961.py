from sys import stdin

# from collections import defaultdict


def sol():
    N, D, K, C = map(int, stdin.readline().split())

    # 당연히 그냥 N개 루프돌면서 K개 검사하면 되긴하는데 ,,,,,,,,,
    # 이게 그러면 O(NK)니까 터짐

    # 어차피 추가 삭제는 양끝에서만 이뤄지니까
    # 카카오 보석상점 문제와 거의 동일하다고 봐도 될

    # 그리고 원형을 완벽하게 구현할필요는 없음
    # 어차피 원형이 필요한 이유는 맨마지막에서 돌아오는 거 위함인데,
    # 그거는 1번에서 K-1번까지만 있으면 됨

    # 1 2 3 4 5 있고 k=3일때
    # (3,4,5) (4,5,1) (5,1,2) 니까 ...
    # 1~K-1번 까지만 뒤에 추가해주면 됨.

    sushi = []

    for _ in range(N):
        num = int(stdin.readline())
        sushi.append(num)

    sushi.extend(sushi[: K - 1])

    answer = -1

    sushi_table = {}

    sushi_table[C] = 1

    # 초기 설정
    for i in range(K):
        sushi_num = sushi[i]

        if sushi_num not in sushi_table:
            sushi_table[sushi_num] = 1
        else:
            sushi_table[sushi_num] += 1

        answer = len(sushi_table.keys())
    # print(sushi)

    prev = 0

    for next_ in range(K, N + K):
        next_ = next_ % N
        sushi_num = sushi[next_]

        prev_num = sushi[prev % N]

        sushi_table[prev_num] -= 1

        if sushi_table[prev_num] == 0:
            del sushi_table[prev_num]

        if sushi_num not in sushi_table:
            sushi_table[sushi_num] = 1
        else:
            sushi_table[sushi_num] += 1

        answer = max(answer, len(sushi_table))

        prev += 1

    return answer


print(sol())
