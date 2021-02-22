from sys import stdin


def ans():
  group_count = 0
  for _ in range(N):
    word = list(stdin.readline().rstrip('\n'))

    # a-z까지 알파벳이 마지막으로 등장한 위치
    # -1이면 등장하지 않음
    frequency = [-1 for _ in range(26)]

    # word가 group word인지 아닌지
    group_flag = True

    for idx, char in enumerate(word):
      # 이전에 등장한 위치와 현재위치가 한칸 이상 차이난다면
      if frequency[ord(char) - 97] != -1 and abs(frequency[ord(char)-97] - idx)>1:
        group_flag = False
      # 이전에 등장한 위치가 한칸차이면 연속적인 등장 혹은 등장한적 없으면
      else:
        frequency[ord(char) - 97] = idx

    if group_flag:
      group_count += 1
    
    # print(frequency)

  return group_count


N = int(stdin.readline())
print(ans())
