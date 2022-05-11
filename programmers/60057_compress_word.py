def solution(s):
    answer = float("inf")

    length = len(s)

    for unit in range(1, length + 1):

        # print("단위 : "+str(unit))
        start = 0
        end = start + unit

        ret = ""
        prev = ""
        counter = 1

        while end <= length:
            t = s[start:end]

            # print(t)

            if t == prev:
                counter += 1
            elif t != prev and counter > 1:
                ret = ret + str(counter) + str(prev)
                counter = 1
            elif t != prev:
                ret += prev
                counter = 1

            prev = t

            start += unit
            end = start + unit

        if counter >= 1:
            if counter == 1:
                ret = ret + str(prev)
            else:
                ret = ret + str(counter) + str(prev)

        if start < length:
            ret = ret + s[start:]

        answer = min(answer, len(ret))
    return answer
