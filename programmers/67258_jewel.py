from collections import defaultdict


def solution(gems):

    number_of_gems = len(set(gems))

    # 일단 모든 구간을 포함하면, 무조건 가능임.
    # 근데 그러면 돈이 너무 많이드니까 줄이는거임..

    # 근데 만약에 왼쪽 안산다고해,
    # 근데 만약에 모든 보석을 살 수 없으면,

    # 거긴 꼭 있어야해

    l = 0
    r = 0

    count = 1

    hold = defaultdict(int)
    hold[gems[0]] = 1

    # 그냥 계속 줄이는거

    answer = (0, len(gems) - 1, len(gems))

    # print(answer)

    # print(f"wanna find {number_of_gems}")

    # length=[[0 for _ in range(len(gems))] for _ in range(len(gems))]

    # for i in range(len(gems)):
    #     for j in range(len(gems)):
    #         length[i][j]=len(set(gems[i:j]))
    try:
        while r < len(gems) and l <= r:

            # print(gems[l:r+1],len(set(gems[l:r+1])))

            if count == number_of_gems:
                if r - l < answer[2]:
                    answer = (l, r, r - l)
                elif r - l == answer[2]:
                    if l < answer[0]:
                        answer = (l, r, r - l)

                l += 1

                hold[gems[l - 1]] -= 1

                if hold[gems[l - 1]] == 0:
                    count -= 1

            else:
                r += 1

                if r >= len(gems):
                    continue

                if hold[gems[r]] == 0:
                    count += 1
                    hold[gems[r]] = 1

                elif hold[gems[r]] > 0:
                    hold[gems[r]] += 1

    except Exception as e:
        print(e)

    return answer[0] + 1, answer[1] + 1


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))