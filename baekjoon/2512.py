from sys import stdin

N = int(stdin.readline())


def sol():
    budgets = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())

    if sum(budgets) <= M:
        return max(budgets)

    left, right = 0, max(budgets)

    answer = 0

    while left <= right:
        mid = (left + right) // 2

        total = 0

        for budget in budgets:
            if budget <= mid:
                total += budget
            else:
                total += mid

        # 상한선을 줄여야함
        if total > M:
            right = mid - 1
        elif total <= M:
            answer = max(answer, mid)
            left = mid + 1

    return answer


print(sol())
