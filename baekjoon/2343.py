from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    answer = int(1e10)
    lessons = list(map(int, stdin.readline().split()))

    left, right = max(lessons), sum(lessons)

    while left <= right:
        mid = (left + right) // 2

        count = 0

        tmp = 0
        for lesson in lessons:

            if tmp == 0:
                tmp += lesson
                count += 1
            else:
                if tmp + lesson > mid:
                    tmp = lesson
                    count += 1
                else:
                    tmp += lesson

        if count > M:

            left = mid + 1
        else:
            answer = min(answer, mid)
            right = mid - 1

    return answer


print(sol())
