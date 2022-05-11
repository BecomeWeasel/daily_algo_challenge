from sys import stdin
from bisect import bisect_left


def lis(arr):
    if not arr:
        return 0

    # C[i] means smallest last number of lis subsequences whose length are i
    INF = float("inf")
    C = [INF for _ in range(len(arr) + 1)]
    C[0] = -INF
    # C[1] = arr[0]
    C[1] = min(arr)
    tmp_longest = 0

    for n in arr:
        if C[tmp_longest] < n:
            tmp_longest += 1
            C[tmp_longest] = n
        else:
            # next_loc = search(1, tmp_longest, n, C)
            next_loc = bisect_left(C, n, 1, tmp_longest)
            C[next_loc] = n

    return tmp_longest


# Find i that matches C[i-1] < n <= C[i]
def search(lo, hi, n, C):
    if lo == hi:
        return lo
    # elif lo + 1 == hi:
    # return lo if C[lo] >= n else hi

    mid = (lo + hi) // 2
    if C[mid] == n:
        return mid
    elif C[mid] < n:
        return search(mid + 1, hi, n, C)
    else:
        return search(lo, mid, n, C)


N = int(stdin.readline())

numbers = list(map(int, stdin.readline().split()))

print(lis(numbers))
