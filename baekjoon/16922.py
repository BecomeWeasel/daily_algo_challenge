from sys import stdin

N = int(stdin.readline())

rome = ("I", "V", "X", "L")

check = set()


def ans():

    #### brute-force #####
    # rome_made = ['I', 'V', 'X', 'L']
    # for i in range(1, N):
    #   new_rome = list()

    #   for prev in rome_made:
    #     for k in range(4):
    #       if not parser(prev + rome[k][0]) in list(map(parser,new_rome)):
    #         new_rome.append(prev + rome[k][0])

    #   rome_made = new_rome
    # print(len(rome_made))
    #####################

    #### back-tracking ####
    result_rome = list()
    dfs(1, "I", result_rome)
    dfs(1, "V", result_rome)
    dfs(1, "X", result_rome)
    dfs(1, "L", result_rome)

    # 결과 리스트에 몇개의 로마 숫자가 있는지 출력
    return len(result_rome)


def dfs(length, current_rome, result_rome):
    # N자리 로마숫자를 완성했으면 결과 리스트에 넣어줌
    if length == N:
        result_rome.append(current_rome)
        return

    for k in range(4):
        # 백트래킹 적용되는 부분
        # 체크리스트에 로마자를 변환한 숫자와 길이가 동시에 있는 이유는
        # IVV와 IX는 둘다 같은 10을 의미하는데 IVV와 IX 모두 방문해야 하기때문에
        # 로마자 숫자의 길이도 기록
        if not (parser(current_rome + rome[k]), length) in check:
            dfs(length + 1, current_rome + rome[k], result_rome)
            check.add((parser(current_rome + rome[k]), length))


# 로마숫자를 10진법 숫자로 변환
def parser(rome_numbers):
    rome_to_num = (("I", 1), ("V", 5), ("X", 10), ("L", 50))

    result = 0
    for char in rome_numbers:
        result += next(x[1] for x in rome_to_num if char == x[0])

    return result


print(ans())
