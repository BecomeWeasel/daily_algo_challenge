from bisect import bisect_left
from sys import stdin


def sol():
    N = int(stdin.readline())
    
    numbers=[]

    for _ in range(N):
        a,b=map(int,stdin.readline().split())
        numbers.append((a,b))

    numbers.sort(key=lambda x: x[0])

    # print(numbers)

    numbers=[x[1] for x in numbers]

    

    length = 0

    
    C = [-float('inf') for _ in range(N+1)]

    for num in numbers:
        if C[length] < num:
            length += 1
            C[length] = num
        else:
            pos = bisect_left(C, num, 0, length)
            C[pos] = num
    # print(C)
    return N-length


print(sol())
