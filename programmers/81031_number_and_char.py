def solution(s):
    answer = ""

    stack = []

    para = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for c in s:
        if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            answer += str(c)
        else:
            stack.append(c)

            if "".join(stack) in para:
                answer += str(para.index("".join(stack)))
                stack = []

    return int(answer)
