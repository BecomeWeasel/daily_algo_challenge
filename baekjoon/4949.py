from sys import stdin


while True:
    s = stdin.readline().rstrip()

    if s == ".":
        break

    def valid(s, stack):
        for char in s:
            if char not in ["[", "]", "(", ")"]:
                continue
            elif char == "]":
                if len(stack) == 0:
                    return "no"
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return "no"
            elif char == ")":
                if len(stack) == 0:
                    return "no"
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return "no"
            else:
                stack.append(char)
        if len(stack) != 0:
            return "no"
        else:
            return "yes"

    print(valid(s, list()))
