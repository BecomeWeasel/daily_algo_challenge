def solution(n, k, cmd):

    cut = [False for _ in range(n)]
    nxt = [-1 for _ in range(n)]
    pre = [-1 for _ in range(n)]

    nxt[0] = 1
    pre[0] = -1

    cur = k

    remove = []

    for i in range(1, n):
        nxt[i] = i + 1
        pre[i] = i - 1

    for order in cmd:
        order_set = order.split(" ")

        if len(order_set) == 1:
            if order_set[0] == "C":
                # 마지막행일경우는 위 행 선택
                if nxt[cur] == n:
                    nxt[pre[cur]] = n
                    remove.append(cur)
                    cut[cur] = True
                    cur = pre[cur]
                else:
                    cut[cur] = True
                    nxt[pre[cur]] = nxt[cur]
                    pre[nxt[cur]] = pre[cur]

                    remove.append(cur)

                    cur = nxt[cur]

            elif order_set[0] == "Z":
                tos = remove.pop()

                if nxt[tos] == n:
                    nxt[pre[tos]] = tos
                else:
                    nxt[pre[tos]] = tos
                    pre[nxt[tos]] = tos

                cut[tos] = False

        else:
            if order_set[0] == "U":
                for _ in range(int(order_set[1])):
                    cur = pre[cur]

            elif order_set[0] == "D":
                for _ in range(int(order_set[1])):
                    cur = nxt[cur]

    answer = ""
    for c in cut:
        if c:
            ret += "X"
        else:
            ret += "O"
    return ret
