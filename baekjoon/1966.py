from sys import stdin

T = int(stdin.readline())


def ans():
    N, target_paper = map(int, stdin.readline().split())
    if N == 1:
        tmp = int(stdin.readline())
        return 1
    print_queue = [[i, 0] for i in range(N)]
    target_paper = print_queue[target_paper][0]
    priority = list(map(int, stdin.readline().split()))

    for idx, item in enumerate(priority):
        print_queue[idx][1] = item

    print_counter = 0
    while len(print_queue) > 0:

        front_priority = print_queue[0][1]
        canPrint = True

        for paper in print_queue:
            if paper[1] > front_priority:

                canPrint = False
                break

        # 맨 앞이 우선순위가 높다면
        # 그냥 출력한다
        if canPrint:
            print_counter += 1

            if target_paper == print_queue[0][0]:
                return print_counter
            else:
                # 출력하고 큐에서 내보냄
                del print_queue[0]

        # 맨 앞 인쇄물이 중요도가 가장높지 않다면
        else:
            # 중요도가 낮은 맨 앞의 것을 뒤로 보낸다.
            paper_num, paper_priority = print_queue[0]
            del print_queue[0]
            print_queue.append([paper_num, paper_priority])


for _ in range(T):
    print(ans())
