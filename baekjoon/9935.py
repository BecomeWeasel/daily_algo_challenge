from sys import stdin


def sol():
    inputs_ = list(stdin.readline().rstrip())
    target = list(stdin.readline().rstrip())
    last = target[-1]
    target_len = len(target)
    stack = list()

    for char in inputs_:
        stack.append(char)

        # 어차피 마지막 문자만 중요하니까
        if char == last and stack[-target_len:] == target:
            del stack[-target_len:]

    print(''.join(stack) if len(stack) != 0 else "FRULA")


sol()