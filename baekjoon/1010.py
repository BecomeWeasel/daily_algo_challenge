import sys
from math import factorial

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    answer = factorial(b) // (factorial(a) * factorial(b - a))
    print(answer)
