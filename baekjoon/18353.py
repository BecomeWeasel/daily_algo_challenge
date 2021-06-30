from bisect import bisect_left
from sys import stdin

N=int(stdin.readline())

def sol():
    numbers=list(map(int,stdin.readline().split()))
    numbers.reverse()

    INF=float('inf')

    C=[-INF for _ in range(len(numbers)+1)]

    C[1]=min(numbers)
    lis_length=0

    for n in numbers:
        if C[lis_length]<n:
            lis_length+=1
            C[lis_length]=n
        else:
            loc=bisect_left(C,n,1,lis_length)
            C[loc]=n
    # print(C)
    return N-lis_length

print(sol())