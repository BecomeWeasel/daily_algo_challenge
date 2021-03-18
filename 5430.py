from sys import stdin
from collections import deque

T = int(stdin.readline())


def sol():
  task_set = stdin.readline().rstrip('\n')
  n = int(stdin.readline())

  if n == 0:
    throw = stdin.readline()
    for task in task_set:
      # 길이가 0인데 한번이라도 삭제명령어가 온다면 에러출력
      if task == 'D':
        print('error')
        return
    # 명령어중에 단 한번이라도 D가 안나오면 그냥 빈배열 거꾸로 출력
    print('[]')
    return

  # 배열 입력받고 홀수번째 idx에 있는것들만 빼오기
  # 이러면 한자리 숫자 밖에 받지못함
  # numbers = [ int(x) for idx, x in enumerate(stdin.readline().rstrip('\n')) if idx % 2 == 1 ]

  numbers = deque(map(int, stdin.readline().rstrip('\n')[1:-1].split(',')))

  # reverse_numbers = numbers[::-1]

  is_set_reverse = False

  for task in task_set:
    # R 명령어가 들어오면
    if task == 'R':
      is_set_reverse = False if is_set_reverse else True
      # reverse_numbers, numbers = numbers, reverse_numbers

    # D 명령어가 들어오면
    else:
      if len(numbers) == 0:
        print('error')
        return 0

      if is_set_reverse:
        numbers.pop()
      else:
        numbers.popleft()

  # print('[' + ','.join(map(str, numbers)) + ']')
  if is_set_reverse:
    print('[' + ','.join(map(str, list(numbers)[::-1])) + ']')
  else:
    print('[' + ','.join(map(str, numbers)) + ']')


for _ in range(T):
  sol()
