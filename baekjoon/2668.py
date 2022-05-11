from sys import stdin


def sol():
    N = int(stdin.readline())

    upper = [i for i in range(N + 1)]
    lower = [-1]
    for _ in range(N):
        lower.append(int(stdin.readline()))

    valid = [True for _ in range(N + 1)]
    valid[0] = False

    while True:
        valid_list = set()
        before_len = sum(1 for x in upper if valid[x])

        for idx, lower_num in enumerate(lower):
            if not valid[idx]:
                continue
            else:
                valid_list.add(lower_num)

        for num in upper:
            if not num in valid_list and valid[num]:
                valid[num] = False

        after_len = sum(1 for x in upper if valid[x])

        if before_len == after_len:
            break

    answer = [i for i in upper if valid[i]]
    answer.sort()
    print(len(answer))
    for num in answer:
        print(num)


sol()
