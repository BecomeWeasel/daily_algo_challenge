from sys import stdin

A, P = map(int, stdin.readline().split())


def ans():
  result = [A]

  while True:
    new_num = 0
    for char in str(result[-1]):
      new_num += int(char)**P

    # 만약 이미 결과 리스트에 들어가있다면 반복이 시작된 것
    # result안에서 그 숫자부터 뒤까지 모든 숫자를 날리고 (반복의 시작이니)
    # result의 길이를 반환
    if new_num in result:
      # start_of_iteration=result.index(new_num)
      # result=result[:start_of_iteration]
      # return len(result)

      return len(result[:result.index(new_num)])

    else:
      result.append(new_num)


print(ans())