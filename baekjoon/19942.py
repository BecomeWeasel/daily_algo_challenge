from sys import stdin
import heapq as hq


def sol():

    N = int(stdin.readline())

    mp, mf, ms, mv = map(int, stdin.readline().split())

    info = []

    for i in range(N):
        p, f, s, v, c = map(int, stdin.readline().split())

        info.append({"p": p, "f": f, "s": s, "v": v, "c": c})

    visit = set()

    answer = []

    def dfs(bit, current, cp, cf, cs, cv, cc):
        nonlocal answer, visit

        if cp >= mp and cf >= mf and cs >= ms and cv >= mv:
            t = []
            for i in range(N):
                if bit & (1 << i):
                    t.append(i)
            t = list(map(lambda x: x + 1, t))
            hq.heappush(answer, (cc, t))
            return

        if answer and cc >= answer[0][0]:
            return

        # 이부분에서 대형실수
        # for i in range(N):
        # 이렇게 짜면 , 지금 현재 3번일때, 1번 다시 보게 됨 ... 그러니까 1->2->4->6 이 된후에 2번이 다시 2->1->4->6 ... 4번이 4->1->2->6 이런 대참사 발생
        for i in range(current + 1, N):
            if bit & (1 << i) == 0:
                next_bit = bit | (1 << i)
                dfs(
                    next_bit,
                    i,
                    cp + info[i]["p"],
                    cf + info[i]["f"],
                    cs + info[i]["s"],
                    cv + info[i]["v"],
                    cc + info[i]["c"],
                )

    # for i in range(N):
    #     dfs(1<<i,i,info[i]["p"],info[i]["f"],info[i]["s"],info[i]["v"],info[i]["c"])
    dfs(0, -1, 0, 0, 0, 0, 0)

    if not answer:
        print(-1)
    else:
        print(answer[0][0])
        print(" ".join(map(str, answer[0][1])))


sol()
