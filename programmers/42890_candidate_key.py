from itertools import combinations


def isRedundant(answer, combi):
    for e in answer:
        if e.issubset(combi):
            return True
    return False


def getMatchCount(relation, query):
    col_N = len(relation[0])
    row_N = len(relation)

    t = 0

    for row in relation:
        match = True
        for col_idx, value in query:
            if str(row[col_idx]) != str(value):
                match = False
                break

        if match:
            t += 1
    return t


def isPossible(combi, relation):
    col_N = len(relation[0])
    row_N = len(relation)

    combi = list(combi)

    for row in relation:
        query = list()

        for e in combi:
            query.append((e, row[e]))

        if getMatchCount(relation, query) > 1:
            return False

    return True


def solution(relation):
    answer = list()

    col_N = len(relation[0])
    row_N = len(relation)

    # print(col_N,row_N)


    for number_of_c in range(1, col_N + 1):
        for combi in combinations(range(col_N), number_of_c):

            combi = list(combi)
            combi.sort()
            combi = set(combi)

            if isRedundant(answer, combi):
                continue

            combi = set(combi)
            if isPossible(combi, relation):
                answer.append(combi)

    return len(answer)
