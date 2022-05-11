from sys import stdin
from functools import cmp_to_key

# 17% 틀립니다

# 반례
# 2 2
# 34
# 344

# ans : 34434
# output : 34344
K, N = map(int, stdin.readline().split())


def sol():
    target = ""

    numbers = []

    for _ in range(K):
        numbers.append(stdin.readline().rstrip())

    # 자릿수가 긴것을 앞으로,자릿수가 같다면 크기가 큰 것
    # 자릿수가 길고 가장 큰것이 가장 많이 사용됨 N-K번
    # 나머지는 다 한번씩만 사용해줘야함
    key = str(max(list(map(int, numbers))))

    for _ in range(N - K):
        numbers.append(key)

    new_numbers = custom_sort(numbers)

    target = "".join(new_numbers)

    # for num in new_numbers:
    #   target+=num

    # if N!=K:
    #   target=target+key*(N-K)

    return int(target)


def custom_digit_compare(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)):
        return 1
    else:
        return -1


# 수정필요
def custom_sort(list_):
    # tmp = []

    # max_len = 0

    # for item in list_:
    #   max_len = max(len(item), max_len)

    # for idx, num in enumerate(list_):
    #   diff = 0

    #   list_num = list(num)

    #   first_digit = int(list_num[0])

    #   # 가장 큰 자리수의 숫자로부터
    #   # 나머지 숫자들이 얼마나 떨어져있는지 기록
    #   # 작을수록 큰 값
    #   for i in range(1, len(list_num)):
    #     diff += first_digit - int(list_num[i])

    #   digit = int(num) % 10

    #   if len(num) < max_len:
    #     tmp.append((idx, num + str(digit) * (max_len - len(num)), diff))
    #   else:
    #     tmp.append((idx, num, diff))

    # # 일의 자리를 연장한 값을 먼저 비교하고
    # # 32  322 같이 연장한 값이 같다면
    # # 위에서 계산한 diff를 그다음 기준
    # tmp.sort(key=lambda x: (-int(x[1]), x[2]))
    # ret = []

    list_ = sorted(
        list_, key=cmp_to_key(lambda a, b: -1 if int(str(a) + str(b)) > int(str(b) + str(a)) else 1)
    )

    return list_

    # for idx, num, diff in tmp:
    #   ret.append(list_[idx])

    # return ret


print(sol())
