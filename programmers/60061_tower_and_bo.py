from sys import stdin
from itertools import permutations

# 17%
K, N = map(int, stdin.readline().split())


def sol():
    target = ""

    numbers = []

    for _ in range(K):
        numbers.append(stdin.readline().rstrip())

    # 자릿수가 긴것을 앞으로,자릿수가 같다면 크기가 큰 것
    # 자릿수가 길고 가장 큰것이 가장 많이 사용됨 N-K번
    # 나머지는 다 한번씩만 사용해줘야함
    numbers.sort(key=lambda x: (-len(x), -int(x)))

    # 가장 자릿수가 길고 그중에서 가장 큰것
    key = numbers[0]

    new_numbers = custom_sort(numbers)

    count = 0
    if N != K:
        for num in new_numbers:
            if count == N:
                break

            if num == key:
                if count + (N - K + 1) > N:
                    target = target + key * (N - count)
                else:
                    target = target + key * (N - K + 1)
                    count += N - K + 1
            else:
                target = target + num
                count += 1
    else:
        for num in new_numbers:
            if count == N:
                break
            target = target + num
            count += 1

    return int(target)


# 수정필요
def custom_sort(list_):
    tmp = []

    max_len = 0
    # 가장 자릿수가 긴 숫자의 자릿수 기록
    for item in list_:
        max_len = max(len(item), max_len)

    for idx, num in enumerate(list_):
        diff = 0

        list_num = list(num)

        first_digit = int(list_num[0])

        # 가장 큰 자리수의 숫자로부터
        # 나머지 숫자들이 얼마나 떨어져있는지 기록
        # 작을수록 큰 값
        # 예를 들어서 32, 322중에서
        # 32의 diff는 1 , 322의 diff는 2이니 32가 더 3에 가까움.
        # 정렬할때 32->322의 순서대로 정렬

        # 34,344는
        # 34의 diff는 -1,344의 diff는 -2이니 344가 더 3에 가깝고 큰값
        # 344->34의 순서대로 정렬
        for i in range(1, len(list_num)):
            diff += first_digit - int(list_num[i])

        digit = int(num) % 10

        if len(num) < max_len:
            tmp.append((idx, num + str(digit) * (max_len - len(num)), diff))
        else:
            tmp.append((idx, num, diff))

    tmp.sort(key=lambda x: (-int(x[1]), x[2]))
    ret = []

    for idx, num, diff in tmp:
        ret.append(list_[idx])

    return ret


print(sol())
