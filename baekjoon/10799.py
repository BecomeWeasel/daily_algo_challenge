from sys import stdin


def sol():

    s = stdin.readline().rstrip()
    answer = 0
    stack = list()
    i = 0
    while i < len(s) - 1:
        # 레이저가 들어오면 현재 스택에 있는 막대기 개수만큼
        # 조각이 추가됨
        if s[i] == '(' and s[i + 1] == ')':
            answer += len(stack)
            i += 2
        # 새로운 막대기의 시작
        elif s[i] == '(' and s[i + 1] != ')':
            stack.append(0)
            answer+=1
            i += 1
        # 막대기 끝
        elif s[i] == ')':
            stack.pop()
            i += 1
    return answer


print(sol())