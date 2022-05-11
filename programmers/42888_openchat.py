from collections import defaultdict

id_mapping = defaultdict(str)


def convert(isIn, id):
    global id_mapping
    name = id_mapping[id]
    if isIn:
        return name + "님이 들어왔습니다."
    else:
        return name + "님이 나갔습니다."


def solution(record):
    global id_mapping
    answer = []

    log = list()

    for r in record:
        c = r.split()

        if len(c) == 2:
            log.append([False, c[1]])

        else:
            id_mapping[c[1]] = c[2]

            if c[0] == "Enter":
                log.append([True, c[1]])

    for l in log:
        answer.append(convert(l[0], l[1]))

    return answer
