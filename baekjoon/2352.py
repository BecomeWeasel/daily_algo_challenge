from sys import stdin
from bisect import bisect_left


def sol():
    n=int(stdin.readline())
    numbers=list(map(int,stdin.readline().split()))

    length=1

    C=[float('inf') for _ in range(n+1)]
    C[0]=-float('inf')
    C[1]=numbers[0]

    for n in numbers:
        if C[length]<n:
            length+=1
            C[length]=n
        else:
            idx=bisect_left(C,n)
            C[idx]=n

    # print(C)
    return length

print(sol())