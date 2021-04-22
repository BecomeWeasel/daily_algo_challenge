from collections import deque


def solution(board, moves):
    answer = 0

    basket = deque()

    horizontal = len(board)
    vertical_len = len(board[0])

    stacks = [deque() for _ in range(horizontal)]

    for j in range(horizontal):
        for i in range(vertical_len - 1, -1, -1):
            if board[i][j] != 0:
                stacks[j].append(board[i][j])

    for move in moves:
        # 뽑을 인형이 없을 경우에
        if len(stacks[move - 1]) == 0:
            continue
        doll = stacks[move - 1].pop()

        if len(basket) != 0 and basket[-1] == doll:
            basket.pop()
            answer += 2
        else:
            basket.append(doll)

    return answer


if __name__ == '__main__':
    print(
        solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1],
                  [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
