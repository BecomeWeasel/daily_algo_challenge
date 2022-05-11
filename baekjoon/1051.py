from sys import stdin

N, M = map(int, stdin.readline().split())


def ans():
    grid = [[0] * M for _ in range(N)]

    for i in range(N):
        grid[i] = list(map(int, stdin.readline().rstrip("\n")))

    # 기본 디폴트 정사각형의 사이즈는
    # 숫자 자체로 1
    MAX_SIZE = 1

    # 아래 for 문은 정사각형의 사이즈가
    # 최소 4 이상인것을 검출
    for i in range(N):
        for j in range(M):
            for width in range(M - 1, 0, -1):
                if i + width >= N or j + width >= M:
                    continue
                if is_square(
                    grid[i][j], grid[i][j + width], grid[i + width][j], grid[i + width][j + width]
                ):
                    MAX_SIZE = max(MAX_SIZE, (width + 1) ** 2)

    return MAX_SIZE


def is_square(a, b, c, d):
    tmp_list = [a, b, c, d]

    # a,b,c,d 모두 같다면 첫번째 원소인 a의 개수가
    # tmp_list 내의 길이와 같음
    return tmp_list.count(tmp_list[0]) == len(tmp_list)


print(ans())
