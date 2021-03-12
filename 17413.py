from sys import stdin

S = stdin.readline().rstrip('\n')


def ans():

  NONE, CURLY, CAHR = 0, 1, 2

  state = NONE

  result_string = ''
  temp_string = ''

  # DFA 풀이

  for char in S:
    # 현재 <(open) 태그 안이 아니고 공백이 아닌 문자이면
    if not state == CURLY and ord(char) != 32 and (ord(char) != 60 and ord(char) != 62):
      state = NONE
      # 단어 모으기 (뒤집기 위해서)
      temp_string += char
    # 공백이 들어오면 리버스한 문자열 덧붙이기
    elif state == NONE and ord(char) == 32:
      # 이전까지 모아둔 단어 뒤집고 덧붙이기
      result_string += temp_string[::-1]
      temp_string = ''

      result_string += ' '

    # 문자열 다음에 "<"가 들어왔을때 state를 NONE으로 돌리고 리버스한 문자열 합치기
    elif state == NONE and ord(char) == 60:
      result_string += temp_string[::-1]
      temp_string = ''

      # <붙이기
      result_string += char
      state = CURLY
    # > (close)가 들어오면 state를 다시 none으로 돌림
    elif state == CURLY and ord(char) == 62:
      result_string += char

      state = NONE
    # < > 사이에 문자가 들어왔을때
    elif state == CURLY and (ord(char) != 60 or ord(char) != 62):
      result_string += char

  result_string += temp_string[::-1]
  print(result_string)


ans()