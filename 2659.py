from sys import stdin

a, b, c, d = map(int, stdin.readline().split())


def ans():
  clock_numbers = list()

  for i in range(1, 10):
    for j in range(1, 10):
      for h in range(1, 10):
        for k in range(1, 10):
          num = get_clock_number(list(map(str, [i, j, h, k])))
          if not num in clock_numbers:
            clock_numbers.append(num)

  clock_numbers.sort()
  target_clock_number = get_clock_number([a, b, c, d])

  return clock_numbers.index(target_clock_number) + 1


def get_clock_number(crosses):

  candidate = list()

  for i in range(4):
    length, j = 0, 0
    number = str()
    while length < 4:
      number += str(crosses[(i + length) % 4])
      length += 1

    candidate.append(number)
  candidate = list(map(int, candidate))
  return sorted(candidate)[0]


print(ans())