from sys import stdin

N = int(stdin.readline())


def ans():

    count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0}
    first = [0 for _ in range(10)]

    for _ in range(N):
        string = stdin.readline().strip()

        l = len(string)

        for idx, c in enumerate(string):
            if idx == 0:
                first[ord(c) - ord("A")] = 1
            count[c] += 10 ** (l - idx - 1)
            # print(count[c])

    count = sorted([(k, v) for k, v in count.items()], key=lambda x: (x[1]), reverse=True)

    # 만약 모든 숫자가 적절히 쓰인다면
    # 0도 쓰긴 해야함
    # 대신에 count가 제일 작은 애가 뒤로가야됨
    if count[-1][1] != 0:
        for i in range(9, -1, -1):
            if first[ord(count[i][0]) - ord("A")] == 0:
                to_back = count[i]
                count.remove(to_back)
                count.append(to_back)
                break

    print(count)

    ret = 0
    for i in range(10):
        print(count[i][1] * (9 - i))
        ret += count[i][1] * (9 - i)

    return ret


print(ans())
