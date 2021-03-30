from sys import stdin

origin_words = stdin.readline().rstrip('\n')


def ans():

  alphabets_counter = [0 for _ in range(26)]

  # origin_words에서 등장한 알파벳 개수 세기
  for char in origin_words:
    alphabets_counter[ord(char) - 65] += 1

  print(alphabets_counter)

  words_len = len(origin_words)
  how_many_alphabets = sum(1 for x in alphabets_counter if x != 0)
  print(how_many_alphabets)

  # 알파벳의 종류가 홀수이고
  if how_many_alphabets % 2 == 1:
    # 모든 알파벳들이 홀수개만 있으면 생성불가
    # 모든 알파벳들의 곱이 홀수라면 모두 홀수라는 뜻
    mul = 1
    for item in alphabets_counter:
      if not item == 0:
        mul *= item

    if not mul % 2 == 0:
      print("I'm Sorry Hansoo")
      return

  i = 0
  j = words_len - 1
  result = ['A' for _ in range(words_len)]
  # 알파벳이 한개 이상 남은것을 앞쪽과 뒤쪽에 배치
  while True:
    for idx, count in enumerate(alphabets_counter):
      if count > 1:
        result=result[:i]+list(chr(idx+65))+result[i+1:]
        result=result[:j]+list(chr(idx+65))+result[j+1:]

        alphabets_counter[idx] -= 2
        j -= 1
        i += 1

    if sum(alphabets_counter) == 0:
      break

    multiple_left = sum(1 for x in alphabets_counter if x != 0)
    # 여러개가 하나도 없다면
    # A부터 가운데에 배치시작
    if multiple_left == 0:
      for idx, count in enumerate(alphabets_counter):
        if count == 1:
          result.insert(i, chr(idx + 65))

    
  print(''.join(result))
  # print(how_many_alphabets)


ans()
