from sys import stdin


def sol():
    N, K = map(int, stdin.readline().split())

    order = list(map(int, stdin.readline().split()))
    pop_count = 0
    size = 0
    multitap = set()
    for i, o in enumerate(order):

        if o in multitap:
            continue
        elif size < N:
            size += 1
            multitap.add(o)
        else:
            max_distance = -1
            victim = -1
            for candidate in multitap:
                # print(candidate)
                dist = float("inf")
                for j, next_num in enumerate(order[i + 1 :]):
                    if next_num == candidate:
                        dist = min(dist, j)
                        break
                if dist == float("inf") or dist > max_distance:
                    max_distance = dist
                    victim = candidate

            multitap.remove(victim)

            pop_count += 1
            multitap.add(o)

    return pop_count


print(sol())
