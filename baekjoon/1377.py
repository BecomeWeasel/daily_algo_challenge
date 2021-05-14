from sys import stdin


def sol():
    # 몇번의 정렬이 필요한지 계산하면됨
    # O(N^2) 방법

    N = int(stdin.readline())
    # 맨 앞에 의미없는 숫자 하나 추가
    numbers = [(-1, 0)]

    for i in range(N):
        numbers.append((int(stdin.readline()), i + 1))

    # 미리 정렬된 배열 구하기
    sorted_numbers = sorted(numbers, key=lambda x: x[0])


    # 정렬이 한번일어날때마다 <- 쪽으로 이동 한번
    # 기존의 인덱스와 정렬된 인덱스끼리 비교해서 
    # 가장 많이 움직인만큼 정렬이 일어난것

    # +1을 더해주는 이유는 정렬이 끝난 후 한번 검토하는 횟수가 있기때문
    return max([b[1] - a[1]
                for a, b in zip(numbers[1:], sorted_numbers[1:])])+1
                


print(sol())
