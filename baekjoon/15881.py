from sys import stdin

n = int(stdin.readline())


def sol():
    answer = 0
    s = stdin.readline().rstrip()
    i = 0
    while i <= n - 4:
        # print(i,s[i:i+4])
        if s[i : i + 4] == "pPAp":
            answer += 1
            i += 4
        else:
            i += 1

    return answer


print(sol())
