def solution(s):
    answer = []

    # # 양 끝 { } 제거 후 exec 으로 실행
    # exec("set_list=" + s[1:-1], globals())

    # list_=list(set_list)

    s = s.lstrip("{").rstrip("}").split("},{")

    list_ = []

    for e in s:
        list_.append(e.split(","))

    if len(list_) == 1:
        answer.append(int(list_[0][0]))
        return answer

    list_ = sorted(list_, key=len)

    for set_ in list_:
        for e in set_:
            if not int(e) in answer:
                answer.append(int(e))

    return answer


if __name__ == "__main__":
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
