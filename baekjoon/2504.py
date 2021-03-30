from sys import stdin
# from collections import deque

words = stdin.readline().rstrip('\n')


def ans():

  stack = l == t()

  state = 0

  for char in words:

    # if isinstance(tos, int) and isinstance(sos, int):
    # stack.append(tos + sos)

    if char == ')':
      if not stack:
        return 0

      if state == 2:
        return 0

      # top of stack
      tos = stack.pop()
      if isinstance(tos, int):
        if not stack:
          return 0
        # second of stack
        sos = stack.pop()
        if sos == '(':
          stack.append(tos * 2)
      # ( ) 완성
      elif tos == '(':
        stack.append(2)
        state = 0
      # ) 전에 온것이 [,],숫자라면 다시 집어넣기
      else:
        stack.append(tos)
        stack.append(char)
    elif char == ']':
      if not stack:
        return 0

      if state == 1:
        return 0
      # top of stack
      tos = stack.pop()

      # [ n ] 이면 3n집어넣기
      if isinstance(tos, int):
        if not stack:
          return 0
        # second of stack
        sos = stack.pop()
        if sos == '[':
          stack.append(tos * 3)
      # [ ] 완성
      elif tos == '[':

        stack.append(3)
        state = 0
      else:

        stack.append(tos)
        stack.append(char)
    else:
      if char == '(':
        state = 1
      elif char == '[':
        state = 2
      stack.append(char)

    # stack_organize(stack)
    copy_list = stack

    for idx, item in enumerate(copy_list):
      if idx >= 1 and isinstance(item, int) and isinstance(
          copy_list[idx - 1], int):
        tos = copy_list.pop()
        sos = copy_list.pop()
        copy_list.append(tos + sos)
    stack = copy_list

  # 스택 안에 처리안된 괄호가 남아있으면
  # 0을 반환
  e = ['(', ')', '[', ']']
  for item in stack:
    if item in e:
      return 0

  # 계산이 끝난 합연산 괄호들 다 더해서 리턴
  return sum(stack)


def bracket_matching(old_stack):
  # 매치되는 괄호들을 삭제시킴
  # 괄호가 남는다면 매칭 안된다는뜻


  # 문자열의 길이가 홀수면 무조건 괄호는 생길수 없음
  if len(old_stack) % 2 == 1:
    return 0

  stack = list()

  for item in old_stack:
    if item == '(' or item == '[':
      stack.append(item)
    elif item == ')' and stack:
      if stack[-1] == '(':
        stack = stack[:-1]
      else:
        stack.append(item)
    elif item == ']' and stack:
      if stack[-1] == '[':
        stack = stack[:-1]
      else:
        stack.append(item)
    else:
      stack.append(item)

  # 처리되지 않은 (매칭되지 않는) 괄호들이 남아있으면 False
  if stack:
    return False
  else:
    return True


def sol():
  stack = list()
  for char in words:
    if char == '(' or char == '[':
      stack.append(char)
    elif char == ')':
      if stack[-1] == '(':

        # del stack[-1]
        # stack.append(2)
        stack[-1] = 2
      else:
        temp = 0

        for i in range(len(stack) - 1, -1, -1):
          if stack[i] == '(':
            stack[-1] = temp * 2
            break
          else:
            temp += stack[i]
            stack.pop()

    elif char == ']':
      if stack[-1] == '[':
        stack[-1] = 3
      else:
        temp = 0
        for i in range(len(stack) - 1, -1, -1):
          if stack[i] == '[':
            stack[-1] = temp * 3
            break
          else:
            temp += stack[i]
            stack.pop()

  # print(stack)

  bracket_list = ['(', '[', ')', ']']

  for item in stack:
    if item in bracket_list:
      return 0

  return sum(stack)


print(sol() if bracket_matching(list(words)) else 0)
