def is_valid(s):
    stack = list()

    for symbol in s:
        if len(stack) == 0:
            stack.append(symbol)
            continue

        if stack[-1] == "(" and symbol == ")":
            stack.pop()
            continue

        stack.append(symbol)

    if len(stack) == 0:
        return True
    else:
        return False


def solution(p):
    if is_valid(p):
        return p

    def solve(p):
        # print("cehck")

        if p == "":
            return ""

        if is_valid(p):
            print("correct and return " + p)
            return p

        l_c, r_c = 0, 0

        u, v = "", ""

        for idx, symbol in enumerate(p):
            if symbol == "(":
                l_c += 1
            else:
                r_c += 1

            if l_c == r_c:
                u = p[: idx + 1]
                v = p[idx + 1 :]
                break

        if is_valid(u):
            return u + solve(v)

        temp = "(" + solve(v) + ")"

        u = u[1:-1]
        u = list(u)
        for idx, symbol in enumerate(u):
            if symbol == "(":
                u[idx] = ")"
            else:
                u[idx] = "("
        temp += "".join(map(str, u))
        return temp

    answer = solve(p)

    return answer
