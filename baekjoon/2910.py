from sys import stdin
import heapq

N, C = map(int, stdin.readline().split())


def ans():
    numbers = list(map(int, stdin.readline().split()))

    counter_and_pos = list()
    # item [0] : 숫자
    # item [1] : 처음 나온 idx
    # item [2] : 몇번 등장

    for idx, number in enumerate(numbers):
        isInList = False
        for item in counter_and_pos:
            # 그 숫자가 이전에 등장한적 있다면
            if number == item[0]:
                item[2] += 1
                isInList = True
                break

        # 이전에 등장한적 없는 숫자라면 새로 추가해줌
        if not isInList:
            counter_and_pos.append([number, idx, 1])

    # 많이 등장한 순서대로, 등장 빈도가 같다면 먼저 등장한 순서대로
    counter_and_pos.sort(reverse=True, key=lambda x: (x[2], -x[1]))

    # print(counter_and_pos)

    result_list = list()
    for info in counter_and_pos:
        for count in range(info[2]):
            result_list.append(info[0])

    print(" ".join(map(str, result_list)))


ans()
