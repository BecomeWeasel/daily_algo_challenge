from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []

    n = len(info)

    person_list = defaultdict(list)

    for i in info:
        i = i.split()
        rank = int(i[4])

        l = [0, 1, 2, 3]
        for count in range(5):
            for combi in combinations(l, count):
                # 아무것도 없는것
                if len(combi) == 0:
                    person_list["----"].append(rank)
                    continue

                s = ""
                for j in l:
                    if j in combi:
                        s += i[j]
                    else:
                        s += "-"
                # print(s)

                person_list[s].append(rank)

        # print(''.join(i[:4]),person_list[''.join(i[:4])])

    for k in person_list.keys():
        person_list[k].sort()

    temp_query = []

    for q in query:
        questions = q.split(" and ")
        t = questions[3].split(" ")
        del questions[3]
        questions.append(t[0])
        questions.append(t[1])
        temp_query.append(questions)

    # print(person_list["----"])

    for query in temp_query:
        target_query = "".join(query[:4])

        answer.append(
            len(person_list[target_query]) - bisect_left(person_list[target_query], int(query[4]))
        )

    # print(person_list["-backend--"])

    return answer
