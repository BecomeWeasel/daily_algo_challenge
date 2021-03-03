from sys import stdin
import math

T = int(stdin.readline())


def ans():
  votes = [[0, i] for i in range(N)]

  for i in range(N):
    votes[i][0] = int(stdin.readline())

  total_votes = sum(x[0] for x in votes)

  votes.sort(key=lambda x: -x[0])

  if (votes[0][0] == votes[1][0]):
    print("no winner")
  elif votes[0][0] > total_votes / 2:
    print("majority winner " + str(votes[0][1] + 1))
  else:
    print("minority winner " + str(votes[0][1] + 1))


for _ in range(T):
  N = int(stdin.readline())
  ans()
