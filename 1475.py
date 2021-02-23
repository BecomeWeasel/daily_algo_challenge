from sys import stdin
import math


def ans():
  counter = [0 for _ in range(10)]

  pair = 0
  for number in numbers:
    if int(number) == 6 or int(number) == 9:
      pair += 1
    else:
      counter[int(number)] += 1
  
  return max(max(counter),math.ceil(pair/2))


numbers = list(stdin.readline().rstrip('\n'))
print(ans())
