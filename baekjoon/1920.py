from sys import stdin

N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
numbers.sort()
M = int(stdin.readline())
target = list(map(int, stdin.readline().split()))


def sol():
    for target_ in target:
        print(binary_search(target_, numbers, 0, len(numbers) - 1))


def binary_search(target, number, left, right):

    while left <= right:
        mid = (left + right) // 2

        if number[mid] == target:
            return 1

        elif number[mid] < target:
            return binary_search(target, number, mid + 1, right)

        else:
            return binary_search(target, number, left, mid - 1)
    return 0


sol()
