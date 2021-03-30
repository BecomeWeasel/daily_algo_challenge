from sys import stdin

N = int(stdin.readline())


def ans():
  result = 0

  digit = len(str(N))

  accumulate_length = 0

  for i in range(1, digit):
    accumulate_length += i * 9 * 10**(i - 1)

  result = accumulate_length + (N - (10**(digit - 1) - 1)) * digit

  return result


print(ans())