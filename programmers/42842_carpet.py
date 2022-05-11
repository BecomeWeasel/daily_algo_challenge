def solution(brown, yellow):
    answer = []

    for y_h in range(1, yellow + 1):
        y_v = int(yellow / y_h)

        b_h, b_v = y_h + 2, y_v + 2

        # 카펫의 가로의 길이는 세로의 길이와 같거나 길다
        if b_h < b_v:
            continue

        if b_h * b_v - yellow == brown:
            return [b_h, b_v]

    return answer


if __name__ == "__main__":
    print(solution(24, 24))
