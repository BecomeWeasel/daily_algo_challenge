from itertools import product, permutations


def solution(user_id, banned_id):
    answer = set()

    # 좀 꼼수를 쓰는 방법
    # 어차피 밴 목록에 있는 아이디는 모두 유저아이디에 있는거라고 했으니
    # 둘의 길이가 같다면 모두 밴(경우의 수 1개)
    # if len(user_id) == len(banned_id):
    #     return 1

    # candidate_list에
    # 각각의 ban_id에 대해서 밴의 대상이 될수도 있는 user_id를 모아놓음
    candidate_list = [
        get_ban_candidate_list(user_id, ban_id) for ban_id in banned_id
    ]

    # 가능한 중복순열을 모두 구함
    product_list = list(product(*candidate_list))

    banned_set = []

    # combi : 밴 리스트의 예비 대상들
    for combi in product_list:
        # 중복되지 않고
        if len(combi) == len(set(combi)):
            unique_value = sum(2**idx for idx in combi)
            
            if unique_value not in answer:
                answer.add(unique_value)

        # if len(set(combi)) == len(banned_id) and not "".join(
        #         list(combi)) in answer:
        #     answer.add("".join(list(sorted(combi))))
        # if len(combi) == len(set(combi)):
        # unique_value = 0

        # 아래 방법은 TLE 처음부터 비트마스크 고려

        # # 2**idx를 사용하는 이유는
        # # idx(user_id안에서의 위치)를 기반으로 중복되었는지 안되었는지 확인가능
        # # frodo,crodo,abc123과
        # # crodo,frodo,abc123는 같음
        # # frodo의 idx는 0,crodo는 2,abc123은 3이므로
        # # frodo,crodo,abc123은 = 1+4+8
        # # crodo,frodo,abc123은 = 4+1+8 이므로
        # # 둘은 같은 것임을 구별가능
        # for id_ in combi:
        #     idx = user_id.index(id_)
        #     unique_value += 2**idx
        # if unique_value not in banned_set:
        #     answer+=1
        #     banned_set.append(unique_value)

    return len(answer)


def get_ban_candidate_list(user_id_set, banned_id):
    candidate = []

    # 비트마스킹을 위해서 처음부터 idx를 이용
    for idx, user_id in enumerate(user_id_set):
        # 길이가 다르다면 아예 같을수 없음
        if len(user_id) != len(banned_id):
            continue

        is_candidate = True

        for char_user, char_banned in zip(user_id, banned_id):
            # 가려진 표시를 제외하고 나머지 부분이 유저부분과 다르다면
            # candidate이 될수 없음
            if char_banned != '*' and char_user != char_banned:
                is_candidate = False

        # idx를 넣어서 리턴
        if is_candidate:
            candidate.append(idx)

    return candidate


if __name__ == '__main__':
    # 가장 시간이 오래걸릴것으로 예상되는 TC
    # print(
    #     solution([
    #         "aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd", "eeeeeeee",
    #         "ffffffff", "gggggggg", "hhhhhhhh"
    #     ], [
    #         "********", "********", "********", "********", "********",
    #         "********", "********", "********"
    #     ]))

    # 예제 3번 TC
    print(
        solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                 ["fr*d*", "*rodo", "******", "******"]))
