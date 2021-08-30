from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    max_courses = [defaultdict(int) for _ in range(max(course) + 1)]

    # for k in combinations([1,2,3],2):

    for c in course:
        for o in orders:
            if c > len(o):
                continue

            for combi in combinations(o, c):
                combi_list = sorted(list(combi))
                max_courses[c][''.join(combi_list)] += 1

    for c in course:

        if len(max_courses[c].values()) == 0:
            continue

        max_ = max(max_courses[c].values())

        if max_ < 2:
            continue

        for k in max_courses[c]:
            if max_courses[c][k] == max_:
                answer.append(k)

    return sorted(answer)