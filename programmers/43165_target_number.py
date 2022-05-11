from collections import deque


def solution(numbers, target):
    answer = 0

    q = deque()

    q.append((-numbers[0], 1))
    q.append((numbers[0], 1))

    while len(q) != 0:
        cumulative, count = q.popleft()

        if count + 1 == len(numbers):
            if cumulative + numbers[-1] == target:
                answer += 1
            elif cumulative - numbers[-1] == target:
                answer += 1
        else:
            q.append((cumulative + numbers[count], count + 1))
            q.append((cumulative - numbers[count], count + 1))

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
