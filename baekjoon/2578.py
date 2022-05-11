from sys import stdin


def ans():
    result = 987654321
    counter = 0
    bingo_counter = 0

    # bingo_map[i][j][0] : i열 j행 숫자
    # bingo_map[i][j][1] : i열 j행 숫자를 사회자가 불렀는지 체크
    bingo_map = [[[0, False] for _ in range(5)] for _ in range(5)]

    for i in range(5):
        added_numbers = list(map(int, stdin.readline().split()))

        for idx, added_number in enumerate(added_numbers):
            bingo_map[i][idx][0] = added_number

    for i in range(5):
        called_numbers = list(map(int, stdin.readline().split()))

        for number in called_numbers:
            # 숫자를 하나 부름
            counter += 1
            for i in range(5):
                for j in range(5):
                    if bingo_map[i][j][0] == number:
                        bingo_map[i][j][1] = True
                        # 가로로 확인

                        if (
                            sum(bingo_map[i][h][1] for h in range(5) if bingo_map[i][h][1] == True)
                            == 5
                        ):
                            bingo_counter += 1

                        # 세로로 확인

                        if (
                            sum(bingo_map[h][j][1] for h in range(5) if bingo_map[h][j][1] == True)
                            == 5
                        ):
                            bingo_counter += 1

                        if bingo_counter + dia_bingo_check(bingo_map) >= 3:
                            return counter


# 대각선 빙고 체크하는 함수
def dia_bingo_check(bingo_map):

    return (
        1 if sum(bingo_map[h][h][1] for h in range(5) if bingo_map[h][h][1] == True) == 5 else 0
    ) + (
        1
        if sum(bingo_map[0 + h][4 - h][1] for h in range(5) if bingo_map[0 + h][4 - h][1] == True)
        == 5
        else 0
    )


print(ans())
