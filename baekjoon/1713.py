from sys import stdin

N = int(stdin.readline())
num_votes = int(stdin.readline())
votes = list(map(int, stdin.readline().split()))


def ans():

    election_table = list()

    for idx, vote_num in enumerate(votes):

        is_exist_on_table = False
        for candidate in election_table:
            # 이미 사진틀에 올라간 후보라면
            # 한 표 추가
            if candidate[1] == vote_num:
                candidate[0] += 1
                is_exist_on_table = True
                break

        # 사진틀에 없는 사람이라면
        if not is_exist_on_table:
            # 사진틀에 이미 다른 후보로 가득차있다는 것
            if len(election_table) >= N:
                # 가장 득표도 적고 오래된 사람 삭제
                del election_table[N - 1]
                # 1표 추가하고 사진틀에 등록하면서 몇번째 등록된 후보인지 적음
                election_table.append([1, vote_num, idx])
            else:
                # 아직 사진틀에 여유가 남아있으면 그냥 사진틀에 추가하기
                election_table.append([1, vote_num, idx])

        # 사진틀을 득표수가 높은것부터, 득표수가 같다면 먼저 등록한게 뒤로 가게끔 정렬
        election_table.sort(reverse=True, key=lambda x: (x[0], x[2]))

    # 출력은 후보 번호가 증가하는 순서대로
    print(" ".join(str(item[1]) for item in sorted(election_table, key=lambda x: x[1])))


ans()
